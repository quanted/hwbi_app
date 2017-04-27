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

    domains = list()
    for domain in Domain.objects.raw('select * from Domains'):
        domains.append(domain)

    # dct = {}
    # dct['description'] = 'hwbi'
    # dct['name'] = 'human well-being index'
    # dct['min'] = 0
    # dct['max'] = 5
    # dct['unit'] = 'hwbi score'
    # dct['type'] = 'int'

    #domains.append(dct)
    return domains


def get_baseline_scores(state=None, county=None):
    """
    HWBI Get baseline scores
    """

    if state is None or county is None:
        return None

    exists = is_state_in_lowercase_dict(state)
    if exists == False:
        return None

    state = state.upper()
    county = county.upper()

    scores = []
    query = "Select SSB.county_FIPS, CO.stateID, ST.[State], CO.county, SSB.ServiceID, SVC.ServiceName, SSB.Score, SVC.description, SVT.serviceType, SVC.name " \
            "From ServiceScores_Baseline SSB, Counties CO, [Services] SVC, States ST, ServiceTypes SVT " \
            "Where SSB.county_FIPS=CO.county_FIPS and UPPER(ST.state)='{0}' and UPPER(CO.county)='{1}' and SSB.serviceID=SVC.serviceID and CO.stateID=ST.stateID and SVC.ServiceTypeID=SVT.ServiceTypeID"

    query = query.format(state, county)
    print(query)

    for score in BaselineScore.objects.raw(query):
        scores.append(score)

    return scores

def get_states_dict():
    '''Get state abbreviation and name dictionary'''
    states = {
        'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AS': 'American Samoa',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DC': 'District of Columbia',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'GU': 'Guam',
        'HI': 'Hawaii',
        'IA': 'Iowa',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'MA': 'Massachusetts',
        'MD': 'Maryland',
        'ME': 'Maine',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MO': 'Missouri',
        'MP': 'Northern Mariana Islands',
        'MS': 'Mississippi',
        'MT': 'Montana',
        'NA': 'National',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'NE': 'Nebraska',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NV': 'Nevada',
        'NY': 'New York',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'PR': 'Puerto Rico',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VA': 'Virginia',
        'VI': 'Virgin Islands',
        'VT': 'Vermont',
        'WA': 'Washington',
        'WI': 'Wisconsin',
        'WV': 'West Virginia',
        'WY': 'Wyoming'
    }
    return states

def is_state_in_list(state=None, county=None):
    """"""
    states = get_states_dict()
    if state in states.values():
        return True
    else:
        return False

def is_state_in_lowercase_dict(state):
    """Check for lowercase state name in lowercase dict"""
    states = get_states_dict()
    lc_states = dict((k.lower(), v.lower()) for k,v in states.items())
    if state.lower() in lc_states.values():
        return True
    else:
        return False




