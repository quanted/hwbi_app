from django.http import HttpResponse
import json

from .models.sqlite_mgr import get_domains
from .models.sqlite_mgr import get_baseline_scores
from .models.sqlite_mgr import get_domain_scores_national
from .models.sqlite_mgr import get_domain_scores_state
from .models.hwbi_calc import HWBICalc
from .models.meta_info import MetaInfo
from .models.meta_info import MetaBase
from .models.sqlite_mgr import get_state_details
from .models.sqlite_mgr import get_county_indicator_data

from django.conf import settings
from django.template import Context
from django.template.loader import get_template
from django.template.loader import render_to_string
from xhtml2pdf import pisa
import os


def get_disc_scores(request):
    """
    HWBI DISC score request api endpoint
    :param request: POST request dictionary object containing keys ['state', 'county']
    :return: baseline and domain scores for the selected county.
    """

    if request.method == 'GET':
        if 'state' not in request.GET or 'county' not in request.GET or 'state_abbr' not in request.GET:
            return HttpResponse(status=400)
        else:
            state = request.GET['state']
            state_abbr = request.GET['state_abbr']
            county = request.GET['county']
    elif request.method == 'POST':
        request_data = json.loads(request.body, encoding='utf-8')
        state = request_data['state']
        state_abbr = request.GET['state_abbr']
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

    state_domains = get_domain_scores_state(state_abbr)
    for s_domain in state_domains:
        for domain in outputs.domains:
            if domain.domainID == s_domain.domainID:
                domain.stateScore = s_domain.score
                break

    nation_domains = get_domain_scores_national()
    for n_domain in nation_domains:
        for domain in outputs.domains:
            if domain.domainID == n_domain.domainID:
                domain.nationScore = n_domain.score
                break

    outputs.statehwbi = get_state_details(state).score

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


def get_indicator_scores(request):
    if request.method == 'GET':
        if 'county' not in request.GET or 'state_abbr' not in request.GET:
            return HttpResponse(status=400)
        else:
            state_abbr = request.GET['state_abbr']
            county = request.GET['county']
    elif request.method == 'POST':
        request_data = json.loads(request.body, encoding='utf-8')
        state_abbr = request.GET['state_abbr']
        county = request_data['county']
    else:
        return HttpResponse(status=404)

    if state_abbr == "" or county == "":
        return HttpResponse(status=400)

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
    meta_state = MetaBase('state', value=state_abbr, description='US State')
    meta_county = MetaBase('county', value=county, description='County')
    inputs.append(meta_state.get_dict())
    inputs.append(meta_county.get_dict())
    result['inputs'] = inputs
    indicators = get_county_indicator_data(state_abbr=state_abbr, county=county)

    response = HttpResponse()
    try:
        output = []
        for indicator in indicators:
            output.append(indicator.get_dict())
        result['outputs'] = output
        rslt = json.dumps(result)
        print(rslt)
        response.content = rslt
    except Exception as e:
        s = str(e)

    return response


def generate_report(request):
    """
    Creates a pdf report from the provided post arguments.
    :param request:
    :return:
    """
    if request.method != "POST":
        return HttpResponse(status=400)

    # data = json.loads(request.body)
    data = {}
    html_template = 'disc/hwbi-disc-report-template.html'
    report_name = 'disc-report.pdf'
    response = HttpResponse(content_type="application/pdf")
    response['Content-Disposition'] = 'attachment;filename="' + report_name + '"'
    template = get_template(html_template)
    html = template.render(data)
    # html = render_to_string(html_template)
    pisa.CreatePDF(html, dest=response, link_callback=link_callback)
    return response


def link_callback(uri, rel):
    """
    Convert HTML URIs to absolute system paths so xhtml2pdf can access those
    resources
    """

    sUrl = settings.STATIC_URL      # Typically /static/
    root = settings.PROJECT_ROOT   # Typically /home/userX/project_static/
    
    if uri.startswith(sUrl):
        path = os.path.join(root, uri.replace(sUrl, ""))
    else:
        return uri

    if not os.path.isfile(path):
        path = os.getcwd() + uri

    if not os.path.isfile(path):
        raise Exception('media URI file not found. File path: ' + str(path))

    return path
