from hwbi_app.models.domains import Domain
from hwbi_app.models.services import Service
from hwbi_app.models.baseline_scores import BaselineScore


def get_services():
    """
    HWBI Get Services
    """
    #return Service.objects.raw('select * from Services')
    services = []
    svcs = Service.objects.raw('select * from Services')
    for svc in Service.objects.raw('select * from Services'):
        services.append(svc.get_dict())

    return services


def get_domains():
    """
    HWBI Get Domains
    """

    domains = []
    for domain in Domain.objects.raw('select * from Domains'):
        domains.append(domain.get_dict())

    dct = {}
    dct['description'] = 'hwbi'
    dct['name'] = 'human well-being index'
    dct['min'] = 0
    dct['max'] = 5
    dct['unit'] = 'hwbi score'
    dct['type'] = 'int'

    domains.append(dct)
    return domains


def get_baseline_scores(state=None, county=None):
    """
    HWBI Get Domains
    """




    scores = []
    query = "Select SSB.county_FIPS, CO.stateID, ST.[State], CO.county, SSB.ServiceID, SVC.ServiceName, SSB.Score, SVC.description, SVT.serviceType " \
            "From ServiceScores_Baseline SSB, Counties CO, [Services] SVC, States ST, ServiceTypes SVT " \
            "Where SSB.county_FIPS=CO.county_FIPS and UPPER(ST.stateID)='{0}' and UPPER(CO.county)='{1}' and SSB.serviceID=SVC.serviceID and CO.stateID=ST.stateID and SVC.ServiceTypeID=SVT.ServiceTypeID"

    for score in BaselineScore.objects.raw('select * from Domains'):
        scores.append(score)
