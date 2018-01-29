from .domains import Domain
from .services import Service
from .baseline_scores import BaselineScore
from .domain_scores_national import DomainScoresNational
from .domain_scores_state import DomainScoresState
from .state import State
from .indicators_county import IndicatorsCounty


def get_services():
    """
    HWBI Get Services
    """
    #return Service.objects.raw('select * from Services')
    services = []
    svcs = Service.objects.raw('select * from Services')
    for svc in Service.objects.raw('select * from Services'):
        #services.append(svc.get_dict())
        services.append(svc)

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
    query = "Select SSB.county_FIPS, CO.stateID, ST.[State], CO.county, SSB.serviceID, SVC.serviceName, SVC.serviceTypeName, SSB.score, SVC.description, SVT.serviceType, SVC.name " \
            "From ServiceScores_Baseline SSB, Counties CO, [Services] SVC, States ST, ServiceTypes SVT " \
            "Where SSB.county_FIPS=CO.county_FIPS and UPPER(ST.state)='{0}' and UPPER(CO.county)='{1}' and SSB.serviceID=SVC.serviceID and CO.stateID=ST.stateID and SVC.serviceTypeID=SVT.serviceTypeID"

    query = query.format(state, county)
    print(query)

    for score in BaselineScore.objects.raw(query):
        scores.append(score)

    return scores

def get_domain_scores_national():
    scores = []
    query = "Select * from Domains_National"
    for score in DomainScoresNational.objects.raw(query):
        scores.append(score)

    return scores


def get_domain_scores_state(state=None):
    if state is None:
        return None
    if (not is_state_abbrev_in_list(state)):
        return None

    scores = []
    query = "Select * from Domains_State where state = '{0}'"
    query = query.format(state)
    for score in DomainScoresState.objects.raw(query):
        scores.append(score)

    return scores


def get_state_details(state=None):
    if state is None:
        return None
    stateDetails = []
    query = "Select * from States where state = '{0}'"
    query = query.format(state)
    for element in State.objects.raw(query):
        stateDetails.append(element)
    return stateDetails[0]


def get_county_indicator_data(state_abbr=None, county=None):
    if state_abbr is None or county is None:
        return None
    county_indicators = []
    query = "SELECT Indicators_County.indicator, Indicators_County.score, Indicators_County.county_FIPS, Counties.county, Counties.stateID " \
            "FROM Indicators_County INNER JOIN Counties ON Indicators_County.county_FIPS == Counties.county_FIPS " \
            "WHERE Counties.county == '{0}' AND Counties.stateID == '{1}';"
    query = query.format(county, state_abbr)
    for element in IndicatorsCounty.objects.raw(query):
        county_indicators.append(element)
    return county_indicators

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

def is_state_abbrev_in_list(state=None):
    """"""
    states = get_states_dict()
    if state in states.keys():
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




