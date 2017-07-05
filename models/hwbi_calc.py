import copy
from .hwbi_outputs import HwbiOutputs, ServiceOut, DomainOut
from .scores import Scores
from .sqlite_mgr import get_services, get_domains
# from .domain_weights import DomainWeights

class HWBICalc:
    """HWBI Scores Model"""
    def __init__(self):
        self.domain_weights = None
        self.scores = dict()
        self.scaled_scores = dict()
        self.connectiontonature = 0.0
        self.culturalfulfillment = 0.0
        self.education = 0.0
        self.health = 0.0
        self.leisuretime = 0.0
        self.livingstandards = 0.0
        self.safetyandsecurity = 0.0
        self.socialcohesion = 0.0

    def calc_run(self, scores, domains):
        self.scaled_scores = Scores()
        scaled_scores = copy.deepcopy(scores)

        outputs = HwbiOutputs()

        db_services = get_services()

        scaled_scores = Scores()
        for name, score in scores.items():
            out_score = ServiceOut()
            out_score.serviceID = score.serviceID
            out_score.name = score.name
            out_score.serviceTypeName = score.serviceType.lower()
            out_score.description = score.description
            out_score.score = score.score
            outputs.scores.append(out_score)
            scaled_scores.__dict__[score.name.lower()] = score.score


        for attr, value in scaled_scores.__dict__.items():
            val = scaled_scores.__dict__[attr]
            scaled_scores.__dict__[attr] = val / 100

        self.scaled_scores.set_dict(scaled_scores.get_dict())

        domain_value = (2.431227
                        + (0.577159 * self.scaled_scores.communityandfaith)
                        + (-1.755944 * self.scaled_scores.activism)
                        + (-0.370377 * self.scaled_scores.redistribution)
                        + (0.465541 * self.scaled_scores.consumption)
                        + (-0.111739 * self.scaled_scores.healthcare)
                        + (-2.388524 * self.scaled_scores.emergencypreparedness)
                        + (-0.524012 * self.scaled_scores.greenspace)
                        + (0.05051 * self.scaled_scores.waterquality)
                        + (-1.934059 * self.scaled_scores.labor)
                        + (0.211648 * self.scaled_scores.education)
                        + (-1.998989 * self.scaled_scores.communityandfaith * self.scaled_scores.emergencypreparedness)
                        + (2.103267 * self.scaled_scores.activism * self.scaled_scores.emergencypreparedness)
                        + (3.222831 * self.scaled_scores.emergencypreparedness * self.scaled_scores.labor)
                        ) * 100
        self.connectiontonature = domain_value

        domain_value = (-0.22391
                        + (2.429595 * self.scaled_scores.communityandfaith)
                        + (-0.100712 * self.scaled_scores.airquality)
                        + (-0.131353 * self.scaled_scores.waterquantity)
                        + (0.084694 * self.scaled_scores.emergencypreparedness)
                        + (0.191835 * self.scaled_scores.education)
                        + (0.09992 * self.scaled_scores.innovation)
                        + (1.280481 * self.scaled_scores.communication)
                        + (-0.097182 * self.scaled_scores.production)
                        + (-4.405586 * self.scaled_scores.communityandfaith * self.scaled_scores.communication)
                        + (0.23472 * self.scaled_scores.communityandfaith * self.scaled_scores.airquality)
                        ) * 100
        self.culturalfulfillment = domain_value


        domain_value = (0.392837
                        + (0.350783 * self.scaled_scores.familyservices)
                        + (0.463786 * self.scaled_scores.communityandfaith)
                        + (-0.48866 * self.scaled_scores.production)
                        + (0.078233 * self.scaled_scores.publicworks)
                        + (-0.441537 * self.scaled_scores.justice)
                        + (0.574752 * self.scaled_scores.activism)
                        + (-0.37372 * self.scaled_scores.consumption)
                        + (0.390576 * self.scaled_scores.redistribution * self.scaled_scores.greenspace)
                        ) * 100
        self.education = domain_value

        domain_value = (0.231086
                        + (0.072714 * self.scaled_scores.familyservices)
                        + (0.194939 * self.scaled_scores.communication)
                        + (0.097708 * self.scaled_scores.labor)
                        + (0.020422 * self.scaled_scores.waterquantity)
                        + (0.095983 * self.scaled_scores.innovation)
                        + (0.04914 * self.scaled_scores.emergencypreparedness)
                        + (0.52497 * self.scaled_scores.communityandfaith)
                        + (0.149127 * self.scaled_scores.justice)
                        + (0.050258 * self.scaled_scores.activism * self.scaled_scores.education)
                        + (-0.866259 * self.scaled_scores.communityandfaith * self.scaled_scores.justice)
                        ) * 100
        self.health = domain_value

        domain_value = (0.506212
                        + (-0.340958 * self.scaled_scores.employment)
                        + (-0.719677 * self.scaled_scores.waterquantity)
                        + (-0.39237 * self.scaled_scores.consumption)
                        + (0.682084 * self.scaled_scores.foodfiberandfuel)
                        + (-0.053742 * self.scaled_scores.waterquality)
                        + (0.138196 * self.scaled_scores.greenspace)
                        + (-0.544925 * self.scaled_scores.education)
                        + (0.577271 * self.scaled_scores.publicworks)
                        + (-0.217388 * self.scaled_scores.communityandfaith)
                        + (0.934746 * self.scaled_scores.activism)
                        + (1.599972 * self.scaled_scores.waterquantity * self.scaled_scores.education)
                        + (0.206249 * self.scaled_scores.finance * self.scaled_scores.communication)
                        + (-1.29474 * self.scaled_scores.publicworks * self.scaled_scores.activism)
                        + (-0.171528 * self.scaled_scores.education * self.scaled_scores.innovation)
                        ) * 100
        self.leisuretime = domain_value

        domain_value = (0.275027
                        + (0.092259 * self.scaled_scores.employment)
                        + (-0.146247 * self.scaled_scores.publicworks)
                        + (0.134713 * self.scaled_scores.labor)
                        + (0.367559 * self.scaled_scores.activism)
                        + (-0.259411 * self.scaled_scores.finance)
                        + (-0.17859 * self.scaled_scores.justice)
                        + (0.078427 * self.scaled_scores.waterquantity)
                        + (-0.024932 * self.scaled_scores.capitalinvestment)
                        + (0.708609 * self.scaled_scores.publicworks * self.scaled_scores.finance)
                        + (-0.038308 * self.scaled_scores.capitalinvestment * self.scaled_scores.waterquality)
                        + (0.177212 * self.scaled_scores.foodfiberandfuel * self.scaled_scores.communication)
                        ) * 100
        self.livingstandards = domain_value

        domain_value = (0.603914
                        + (0.294092 * self.scaled_scores.communityandfaith)
                        + (-0.380562 * self.scaled_scores.waterquality)
                        + (-0.385317 * self.scaled_scores.publicworks)
                        + (0.085398 * self.scaled_scores.waterquantity)
                        + (1.35322 * self.scaled_scores.activism * self.scaled_scores.labor)
                        + (-0.304328 * self.scaled_scores.production * self.scaled_scores.healthcare)
                        + (-1.147411 * self.scaled_scores.labor * self.scaled_scores.justice)
                        + (0.295058 * self.scaled_scores.production * self.scaled_scores.foodfiberandfuel)
                        + (-0.742299 * self.scaled_scores.greenspace * self.scaled_scores.emergencypreparedness)
                        + (-0.602264 * self.scaled_scores.activism * self.scaled_scores.finance)
                        + (0.898598 * self.scaled_scores.justice * self.scaled_scores.emergencypreparedness)
                        + (0.574027 * self.scaled_scores.publicworks * self.scaled_scores.finance)
                        + (0.655645 * self.scaled_scores.waterquality * self.scaled_scores.publicworks)
                        ) * 100
        self.safetyandsecurity = domain_value

        domain_value = (-0.810156
                        + (1.07278 * self.scaled_scores.justice)
                        + (0.042486 * self.scaled_scores.airquality)
                        + (-0.382991 * self.scaled_scores.production)
                        + (1.980596 * self.scaled_scores.communityandfaith)
                        + (0.047261 * self.scaled_scores.publicworks)
                        + (1.282272 * self.scaled_scores.redistribution)
                        + (0.100406 * self.scaled_scores.capitalinvestment)
                        + (0.152944 * self.scaled_scores.familyservices)
                        + (0.120707 * self.scaled_scores.labor)
                        + (1.291316 * self.scaled_scores.greenspace)
                        + (-0.148073 * self.scaled_scores.consumption)
                        + (-3.59425 * self.scaled_scores.communityandfaith * self.scaled_scores.redistribution)
                        + (-2.048002 * self.scaled_scores.justice * self.scaled_scores.greenspace)
                        + (-0.036457 * self.scaled_scores.employment * self.scaled_scores.waterquality)
                        ) * 100
        self.socialcohesion = domain_value

        db_domains = get_domains()

        total_wt = 0.0

        domains_dict = domains.get_dict()
        for key in domains_dict:
            total_wt += domains_dict[key]

        hwbi = 0.0

        hwbi += self.connectiontonature * domains_dict['connectiontonature']

        hwbi += self.culturalfulfillment * domains_dict['culturalfulfillment']

        hwbi += self.education * domains_dict['education']

        hwbi += self.health * domains_dict['health']

        hwbi += self.leisuretime * domains_dict['leisuretime']

        hwbi += self.livingstandards * domains_dict['livingstandards']

        hwbi += self.safetyandsecurity * domains_dict['safetyandsecurity']

        hwbi += self.socialcohesion * domains_dict['socialcohesion']

        hwbi /= total_wt



        for db_domain in db_domains:
            out_domain = DomainOut()
            out_domain.score = db_domain.score
            out_domain.description = db_domain.name
            out_domain.domainID = db_domain.domainID
            out_domain.domainName = db_domain.domainName
            dct = domains.get_dict()
            out_domain.weight = dct[db_domain.name.lower()]
            outputs.domains.append(out_domain)


        #outputs.hwbi = hwbi
        return hwbi

    def hwbi_run(self, scores, domains):
        #Have to divide these guys by 100
        outputs = HwbiOutputs()

        # Sum up the total for all the weights
        total_wt = 0.0
        for domain in domains:
            total_wt = total_wt + domain.weight

        scaled_scores = Scores()
        for score in scores:
            scaled_scores.__dict__[score.name.lower()] = score.score

        self.scaled_scores = scaled_scores

        for attr, value in scaled_scores.__dict__.items():
            val = scaled_scores.__dict__[attr]
            scaled_scores.__dict__[attr] = val / 100

        self.scaled_scores.set_dict(scaled_scores.get_dict())

        domain_value = 0.0

        domain_value = (2.431227
                        + (0.577159 * self.scaled_scores.communityandfaith)
                        + (-1.755944 * self.scaled_scores.activism)
                        + (-0.370377 * self.scaled_scores.redistribution)
                        + (0.465541 * self.scaled_scores.consumption)
                        + (-0.111739 * self.scaled_scores.healthcare)
                        + (-2.388524 * self.scaled_scores.emergencypreparedness)
                        + (-0.524012 * self.scaled_scores.greenspace)
                        + (0.05051 * self.scaled_scores.waterquality)
                        + (-1.934059 * self.scaled_scores.labor)
                        + (0.211648 * self.scaled_scores.education)
                        + (-1.998989 * self.scaled_scores.communityandfaith * self.scaled_scores.emergencypreparedness)
                        + (2.103267 * self.scaled_scores.activism * self.scaled_scores.emergencypreparedness)
                        + (3.222831 * self.scaled_scores.emergencypreparedness * self.scaled_scores.labor)
                        ) * 100
        self.connectiontonature = domain_value
        lst = list(filter(lambda x: x.name.lower() == 'connectiontonature', domains))
        lst[0].score = self.connectiontonature

        domain_value = (-0.22391
                        + (2.429595 * self.scaled_scores.communityandfaith)
                        + (-0.100712 * self.scaled_scores.airquality)
                        + (-0.131353 * self.scaled_scores.waterquantity)
                        + (0.084694 * self.scaled_scores.emergencypreparedness)
                        + (0.191835 * self.scaled_scores.education)
                        + (0.09992 * self.scaled_scores.innovation)
                        + (1.280481 * self.scaled_scores.communication)
                        + (-0.097182 * self.scaled_scores.production)
                        + (-4.405586 * self.scaled_scores.communityandfaith * self.scaled_scores.communication)
                        + (0.23472 * self.scaled_scores.communityandfaith * self.scaled_scores.airquality)
                        ) * 100
        self.culturalfulfillment = domain_value
        lst = list(filter(lambda x: x.name.lower() == 'culturalfulfillment', domains))
        lst[0].score = self.culturalfulfillment


        domain_value = (0.392837
                        + (0.350783 * self.scaled_scores.familyservices)
                        + (0.463786 * self.scaled_scores.communityandfaith)
                        + (-0.48866 * self.scaled_scores.production)
                        + (0.078233 * self.scaled_scores.publicworks)
                        + (-0.441537 * self.scaled_scores.justice)
                        + (0.574752 * self.scaled_scores.activism)
                        + (-0.37372 * self.scaled_scores.consumption)
                        + (0.390576 * self.scaled_scores.redistribution * self.scaled_scores.greenspace)
                        ) * 100
        self.education = domain_value
        lst = list(filter(lambda x: x.name.lower() == 'education', domains))
        lst[0].score = self.education

        domain_value = (0.231086
                        + (0.072714 * self.scaled_scores.familyservices)
                        + (0.194939 * self.scaled_scores.communication)
                        + (0.097708 * self.scaled_scores.labor)
                        + (0.020422 * self.scaled_scores.waterquantity)
                        + (0.095983 * self.scaled_scores.innovation)
                        + (0.04914 * self.scaled_scores.emergencypreparedness)
                        + (0.52497 * self.scaled_scores.communityandfaith)
                        + (0.149127 * self.scaled_scores.justice)
                        + (0.050258 * self.scaled_scores.activism * self.scaled_scores.education)
                        + (-0.866259 * self.scaled_scores.communityandfaith * self.scaled_scores.justice)
                        ) * 100
        self.health = domain_value
        lst = list(filter(lambda x: x.name.lower() == 'health', domains))
        lst[0].score = self.health

        domain_value = (0.506212
                        + (-0.340958 * self.scaled_scores.employment)
                        + (-0.719677 * self.scaled_scores.waterquantity)
                        + (-0.39237 * self.scaled_scores.consumption)
                        + (0.682084 * self.scaled_scores.foodfiberandfuel)
                        + (-0.053742 * self.scaled_scores.waterquality)
                        + (0.138196 * self.scaled_scores.greenspace)
                        + (-0.544925 * self.scaled_scores.education)
                        + (0.577271 * self.scaled_scores.publicworks)
                        + (-0.217388 * self.scaled_scores.communityandfaith)
                        + (0.934746 * self.scaled_scores.activism)
                        + (1.599972 * self.scaled_scores.waterquantity * self.scaled_scores.education)
                        + (0.206249 * self.scaled_scores.finance * self.scaled_scores.communication)
                        + (-1.29474 * self.scaled_scores.publicworks * self.scaled_scores.activism)
                        + (-0.171528 * self.scaled_scores.education * self.scaled_scores.innovation)
                        ) * 100
        self.leisuretime = domain_value
        lst = list(filter(lambda x: x.name.lower() == 'leisuretime', domains))
        lst[0].score = self.leisuretime

        domain_value = (0.275027
                        + (0.092259 * self.scaled_scores.employment)
                        + (-0.146247 * self.scaled_scores.publicworks)
                        + (0.134713 * self.scaled_scores.labor)
                        + (0.367559 * self.scaled_scores.activism)
                        + (-0.259411 * self.scaled_scores.finance)
                        + (-0.17859 * self.scaled_scores.justice)
                        + (0.078427 * self.scaled_scores.waterquantity)
                        + (-0.024932 * self.scaled_scores.capitalinvestment)
                        + (0.708609 * self.scaled_scores.publicworks * self.scaled_scores.finance)
                        + (-0.038308 * self.scaled_scores.capitalinvestment * self.scaled_scores.waterquality)
                        + (0.177212 * self.scaled_scores.foodfiberandfuel * self.scaled_scores.communication)
                        ) * 100
        self.livingstandards = domain_value
        lst = list(filter(lambda x: x.name.lower() == 'livingstandards', domains))
        lst[0].score = self.livingstandards

        domain_value = (0.603914
                        + (0.294092 * self.scaled_scores.communityandfaith)
                        + (-0.380562 * self.scaled_scores.waterquality)
                        + (-0.385317 * self.scaled_scores.publicworks)
                        + (0.085398 * self.scaled_scores.waterquantity)
                        + (1.35322 * self.scaled_scores.activism * self.scaled_scores.labor)
                        + (-0.304328 * self.scaled_scores.production * self.scaled_scores.healthcare)
                        + (-1.147411 * self.scaled_scores.labor * self.scaled_scores.justice)
                        + (0.295058 * self.scaled_scores.production * self.scaled_scores.foodfiberandfuel)
                        + (-0.742299 * self.scaled_scores.greenspace * self.scaled_scores.emergencypreparedness)
                        + (-0.602264 * self.scaled_scores.activism * self.scaled_scores.finance)
                        + (0.898598 * self.scaled_scores.justice * self.scaled_scores.emergencypreparedness)
                        + (0.574027 * self.scaled_scores.publicworks * self.scaled_scores.finance)
                        + (0.655645 * self.scaled_scores.waterquality * self.scaled_scores.publicworks)
                        ) * 100
        self.safetyandsecurity = domain_value
        lst = list(filter(lambda x: x.name.lower() == 'safetyandsecurity', domains))
        lst[0].score = self.safetyandsecurity

        domain_value = (-0.810156
                        + (1.07278 * self.scaled_scores.justice)
                        + (0.042486 * self.scaled_scores.airquality)
                        + (-0.382991 * self.scaled_scores.production)
                        + (1.980596 * self.scaled_scores.communityandfaith)
                        + (0.047261 * self.scaled_scores.publicworks)
                        + (1.282272 * self.scaled_scores.redistribution)
                        + (0.100406 * self.scaled_scores.capitalinvestment)
                        + (0.152944 * self.scaled_scores.familyservices)
                        + (0.120707 * self.scaled_scores.labor)
                        + (1.291316 * self.scaled_scores.greenspace)
                        + (-0.148073 * self.scaled_scores.consumption)
                        + (-3.59425 * self.scaled_scores.communityandfaith * self.scaled_scores.redistribution)
                        + (-2.048002 * self.scaled_scores.justice * self.scaled_scores.greenspace)
                        + (-0.036457 * self.scaled_scores.employment * self.scaled_scores.waterquality)
                        ) * 100
        self.socialcohesion = domain_value
        lst = list(filter(lambda x: x.name.lower() == 'socialcohesion', domains))
        lst[0].score = self.socialcohesion

        hwbi = 0.0

        lst = list(filter(lambda x: x.name.lower() == 'connectiontonature', domains))
        hwbi += self.connectiontonature * lst[0].weight

        lst = list(filter(lambda x: x.name.lower() == 'culturalfulfillment', domains))
        hwbi += self.culturalfulfillment * lst[0].weight

        lst = list(filter(lambda x: x.name.lower() == 'education', domains))
        hwbi += self.education * lst[0].weight

        lst = list(filter(lambda x: x.name.lower() == 'health', domains))
        hwbi += self.health * lst[0].weight

        lst = list(filter(lambda x: x.name.lower() == 'leisuretime', domains))
        hwbi += self.leisuretime * lst[0].weight

        lst = list(filter(lambda x: x.name.lower() == 'livingstandards', domains))
        hwbi += self.livingstandards * lst[0].weight

        lst = list(filter(lambda x: x.name.lower() == 'safetyandsecurity', domains))
        hwbi += self.safetyandsecurity * lst[0].weight

        lst = list(filter(lambda x: x.name.lower() == 'socialcohesion', domains))
        hwbi += self.socialcohesion * lst[0].weight

        hwbi /= total_wt
        outputs.hwbi = hwbi

        lst_domains = list()
        for domain in domains:
            if isinstance(domain, DomainOut):
                lst_domains.append(domain)
            else:
                lst_domains.append(domain.get_domain_out())

        lst_scores = list()
        for svc in scores:
            if isinstance(svc, ServiceOut):
                lst_scores.append(svc)
            else:
                lst_scores.append(svc.get_service_out())

        outputs.domains = lst_domains
        outputs.services = lst_scores
        return outputs

