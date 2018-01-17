from django.http import HttpResponse
import json

from .models.sqlite_mgr import get_domains
from .models.sqlite_mgr import get_baseline_scores
from .models.hwbi_calc import HWBICalc
from .models.meta_info import MetaInfo
from .models.meta_info import MetaBase


def get_disc_scores(request):
    """
    HWBI DISC score request api endpoint
    :param request: POST request dictionary object containing keys ['state', 'county']
    :return: baseline and domain scores for the selected county.
    """

    if request.method == 'GET':
        if 'state' not in request.GET or 'county' not in request.GET:
            return HttpResponse(status=400)
        else:
            state = request.GET['state']
            county = request.GET['county']
    elif request.method == 'POST':
        request_data = json.loads(request.body, encoding='utf-8')
        state = request_data['state']
        county = request_data['county']
    else:
        return HttpResponse(status=404)

    if state == "" or county == "":
        return HttpResponse(status=400)

    services = list()
    base_line_scores = get_baseline_scores(state, county)
    for base_score in base_line_scores:
        services.append(base_score.get_service_out())

    domains = list()
    db_domains = get_domains()
    for domain in db_domains:
        domains.append(domain.get_domain_out())

    calc = HWBICalc()
    outputs = calc.hwbi_run(services, domains)

    result = dict()
    mi = MetaInfo()
    mi.description = "The Human Well-Being Index (HWBI) model calculator (calc) " \
                     "uses 22 economic, ecosystem, and social services values to " \
                     "calculate eight 'domains of well-being': Connection to Nature, " \
                     "Cultural Fulfillment, Education, Health, Leisure Time, Living " \
                     "Standards, Safety & Security, and Social Cohesion. These domains " \
                     "of well-being are then weighed based on user-supplied 'relative " \
                     "importance values' and are used to determine the overall HWBI score."

    mi.url.href = request.get_full_path()

    result['metaInfo'] = mi.get_dict()

    # build inputs
    inputs = list()
    meta_state = MetaBase('state', value=state, description='US State')
    meta_county = MetaBase('county', value=county, description='County')
    inputs.append(meta_state.get_dict())
    inputs.append(meta_county.get_dict())
    result['inputs'] = inputs

    response = HttpResponse()
    try:
        result['outputs'] = outputs.get_dict()
        rslt = json.dumps(result)
        print(rslt)
        response.content = rslt
    except Exception as e:
        s = str(e)

    return response
