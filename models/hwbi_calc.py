import copy
from hwbi_outputs import HwbiOutputs, ScoreOut, DomainOut
from scores import Scores
from domain_weights import DomainWeights

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


        for attr, value in scaled_scores.__dict__.items():
            val = scaled_scores.__dict__[attr]
            scaled_scores.__dict__[attr] = val / 100

        self.scaled_scores.set_dict(scaled_scores.get_dict())

        self.connectiontonature = (2.431227
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



        self.culturalfulfillment = (-0.22391
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

        self.education = (0.392837
                      + (0.350783 * self.scaled_scores.familyservices)
                      + (0.463786 * self.scaled_scores.communityandfaith)
                      + (-0.48866 * self.scaled_scores.production)
                      + (0.078233 * self.scaled_scores.publicworks)
                      + (-0.441537 * self.scaled_scores.justice)
                      + (0.574752 * self.scaled_scores.activism)
                      + (-0.37372 * self.scaled_scores.consumption)
                      + (0.390576 * self.scaled_scores.redistribution * self.scaled_scores.greenspace)
                      ) * 100

        self.health = (0.231086
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

        self.leisuretime = (0.506212
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

        self.livingstandards = (0.275027
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

        self.safetyandsecurity = (0.603914
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

        self.socialcohesion = (-0.810156
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
        #outputs.hwbi = hwbi
        return hwbi

    def location_run(self, scores, domains):
        #Have to divide these guys by 100
        outputs = HwbiOutputs()

        # Sum up the total for all the weights
        total_wt = 0.0
        for domain in domains:
            out_domain = DomainOut()
            out_domain.score = domain.score
            out_domain.weight = domain.weight
            out_domain.description = domain.name
            out_domain.domainID = domain.domainID
            out_domain.domainName = domain.domainName
            total_wt = total_wt + domain.weight
            outputs.domains.append(out_domain)


        scaled_scores = Scores()
        for score in scores:
            out_score = ScoreOut()
            out_score.serviceID = score.serviceID
            out_score.name = score.name
            out_score.serviceType = score.serviceType.lower()
            out_score.description = score.description
            out_score.Score = score.score
            outputs.scores.append(out_score)
            scaled_scores.__dict__[score.name.lower()] = score.score


        #self.scores = copy.deepcopy(scores)
        self.scaled_scores = scaled_scores

        #self.domain_weights = copy.deepcopy(domain_weights)



        #Sum up the total for all the weights
        #total_wt = 0.0
        #for attr, value in self.domain_weights.__dict__.iteritems():
        #    val = self.domain_weights.__dict__[attr]
        #    total_wt += val

        try:
            # Divide scores by 100 for calc purposes
            for attr, value in self.scaled_scores.__dict__.items():
                val = self.scaled_scores.__dict__[attr]
                self.scaled_scores.__dict__[attr] = val / 100

            self.connectiontonature =   (2.431227
                                   + (0.577159   * self.scaled_scores.communityandfaith)
                                   + (-1.755944  * self.scaled_scores.activism)
                                   + (-0.370377  * self.scaled_scores.redistribution)
                                   + (0.465541   * self.scaled_scores.consumption)
                                   + (-0.111739  * self.scaled_scores.healthcare)
                                   + (-2.388524  * self.scaled_scores.emergencypreparedness)
                                   + ( -0.524012 * self.scaled_scores.greenspace)
                                   + (0.05051    * self.scaled_scores.waterquality)
                                   + (-1.934059  * self.scaled_scores.labor)
                                   + (0.211648   * self.scaled_scores.education)
                                   + (-1.998989  * self.scaled_scores.communityandfaith * self.scaled_scores.emergencypreparedness)
                                   + (2.103267   * self.scaled_scores.activism * self.scaled_scores.emergencypreparedness)
                                   + (3.222831   * self.scaled_scores.emergencypreparedness * self.scaled_scores.labor)
                                    ) * 100

        except Exception as e:
            s = str(e)

        self.culturalfulfillment =  (-0.22391
                                    + (2.429595  * self.scaled_scores.communityandfaith)
                                    + (-0.100712 * self.scaled_scores.airquality)
                                    + (-0.131353 * self.scaled_scores.waterquantity)
                                    + (0.084694  * self.scaled_scores.emergencypreparedness)
                                    + (0.191835  * self.scaled_scores.education)
                                    + (0.09992   * self.scaled_scores.innovation)
                                    + (1.280481  * self.scaled_scores.communication)
                                    + (-0.097182 * self.scaled_scores.production)
                                    + (-4.405586 * self.scaled_scores.communityandfaith * self.scaled_scores.communication)
                                    + (0.23472   * self.scaled_scores.communityandfaith * self.scaled_scores.airquality)
                                    ) * 100

        self.education =    (0.392837
                        + (0.350783 * self.scaled_scores.familyservices)
                        + (0.463786 * self.scaled_scores.communityandfaith)
                        + (-0.48866 * self.scaled_scores.production)
                        + (0.078233 * self.scaled_scores.publicworks)
                        + (-0.441537* self.scaled_scores.justice)
                        + (0.574752 * self.scaled_scores.activism)
                        + (-0.37372 * self.scaled_scores.consumption)
                        + (0.390576 * self.scaled_scores.redistribution * self.scaled_scores.greenspace)
                            ) * 100

        self.health =   (0.231086
                        + (0.072714 * self.scaled_scores.familyservices)
                        + (0.194939 * self.scaled_scores.communication)
                        + (0.097708 * self.scaled_scores.labor)
                        + (0.020422 * self.scaled_scores.waterquantity)
                        + (0.095983 * self.scaled_scores.innovation)
                        + (0.04914  * self.scaled_scores.emergencypreparedness)
                        + (0.52497  * self.scaled_scores.communityandfaith)
                        + (0.149127 * self.scaled_scores.justice)
                        + (0.050258 * self.scaled_scores.activism * self.scaled_scores.education)
                        + (-0.866259 * self.scaled_scores.communityandfaith * self.scaled_scores.justice)
                        ) * 100

        self.leisuretime =  (0.506212
                            + (-0.340958 * self.scaled_scores.employment)
                            + (-0.719677 * self.scaled_scores.waterquantity)
                            + (-0.39237  * self.scaled_scores.consumption)
                            + (0.682084  * self.scaled_scores.foodfiberandfuel)
                            + (-0.053742 * self.scaled_scores.waterquality)
                            + (0.138196  * self.scaled_scores.greenspace)
                            + (-0.544925 * self.scaled_scores.education)
                            + (0.577271  * self.scaled_scores.publicworks)
                            + (-0.217388 * self.scaled_scores.communityandfaith)
                            + (0.934746  * self.scaled_scores.activism)
                            + (1.599972  * self.scaled_scores.waterquantity * self.scaled_scores.education)
                            + (0.206249  * self.scaled_scores.finance * self.scaled_scores.communication)
                            + (-1.29474  * self.scaled_scores.publicworks * self.scaled_scores.activism)
                            + (-0.171528 * self.scaled_scores.education * self.scaled_scores.innovation)
                            ) * 100


        self.livingstandards =  (0.275027
                                + (0.092259  * self.scaled_scores.employment)
                                + (-0.146247 * self.scaled_scores.publicworks)
                                + (0.134713  * self.scaled_scores.labor)
                                + (0.367559  * self.scaled_scores.activism)
                                + (-0.259411 * self.scaled_scores.finance)
                                + (-0.17859 * self.scaled_scores.justice)
                                + (0.078427  * self.scaled_scores.waterquantity)
                                + (-0.024932 * self.scaled_scores.capitalinvestment)
                                + (0.708609  * self.scaled_scores.publicworks * self.scaled_scores.finance)
                                + (-0.038308 * self.scaled_scores.capitalinvestment * self.scaled_scores.waterquality)
                                + (0.177212  * self.scaled_scores.foodfiberandfuel * self.scaled_scores.communication)
                                ) * 100

        self.safetyandsecurity =    (0.603914
                                    + (0.294092  * self.scaled_scores.communityandfaith)
                                    + (-0.380562 * self.scaled_scores.waterquality)
                                    + (-0.385317 * self.scaled_scores.publicworks)
                                    + (0.085398  * self.scaled_scores.waterquantity)
                                    + (1.35322   * self.scaled_scores.activism * self.scaled_scores.labor)
                                    + (-0.304328 * self.scaled_scores.production * self.scaled_scores.healthcare)
                                    + (-1.147411 * self.scaled_scores.labor * self.scaled_scores.justice)
                                    + (0.295058  * self.scaled_scores.production * self.scaled_scores.foodfiberandfuel)
                                    + (-0.742299 * self.scaled_scores.greenspace * self.scaled_scores.emergencypreparedness)
                                    + (-0.602264 * self.scaled_scores.activism * self.scaled_scores.finance)
                                    + (0.898598  * self.scaled_scores.justice * self.scaled_scores.emergencypreparedness)
                                    + (0.574027  * self.scaled_scores.publicworks * self.scaled_scores.finance)
                                    + (0.655645  * self.scaled_scores.waterquality * self.scaled_scores.publicworks)
                                    ) * 100

        self.socialcohesion =   (-0.810156
                                + (1.07278  * self.scaled_scores.justice)
                                + (0.042486 * self.scaled_scores.airquality)
                                + (-0.382991* self.scaled_scores.production)
                                + (1.980596 * self.scaled_scores.communityandfaith)
                                + (0.047261 * self.scaled_scores.publicworks)
                                + (1.282272 * self.scaled_scores.redistribution)
                                + (0.100406 * self.scaled_scores.capitalinvestment)
                                + (0.152944 * self.scaled_scores.familyservices)
                                + (0.120707 * self.scaled_scores.labor)
                                + (1.291316 * self.scaled_scores.greenspace)
                                + (-0.148073* self.scaled_scores.consumption)
                                + (-3.59425 * self.scaled_scores.communityandfaith * self.scaled_scores.redistribution)
                                + (-2.048002* self.scaled_scores.justice * self.scaled_scores.greenspace)
                                + (-0.036457* self.scaled_scores.employment * self.scaled_scores.waterquality)
                                ) * 100



        hwbi = 0.0
        #hwbi += self.connectiontonature * self.domain_weights.connectiontonature

        hwbi += self.connectiontonature * next((x for x in outputs.domains if x.domainID == 'Connection'), None).weight
        next((x for x in outputs.domains if x.domainID == 'Connection'), None).score = self.connectiontonature

        hwbi += self.culturalfulfillment * next((x for x in outputs.domains if x.domainID == 'Culture'), None).weight
        next((x for x in outputs.domains if x.domainID == 'Culture'), None).score = self.culturalfulfillment

        hwbi += self.education * next((x for x in outputs.domains if x.domainID == 'Education'), None).weight
        next((x for x in outputs.domains if x.domainID == 'Education'), None).score = self.education

        hwbi += self.health * next((x for x in outputs.domains if x.domainID == 'Health'), None).weight
        next((x for x in outputs.domains if x.domainID == 'Health'), None).score = self.health

        hwbi += self.leisuretime * next((x for x in outputs.domains if x.domainID == 'Leisure'), None).weight
        next((x for x in outputs.domains if x.domainID == 'Leisure'), None).score = self.leisuretime

        hwbi += self.livingstandards * next((x for x in outputs.domains if x.domainID == 'Living'), None).weight
        next((x for x in outputs.domains if x.domainID == 'Living'), None).score = self.livingstandards

        hwbi += self.safetyandsecurity * next((x for x in outputs.domains if x.domainID == 'Safety'), None).weight
        next((x for x in outputs.domains if x.domainID == 'Safety'), None).score = self.safetyandsecurity

        hwbi += self.socialcohesion * next((x for x in outputs.domains if x.domainID == 'Social'), None).weight
        next((x for x in outputs.domains if x.domainID == 'Social'), None).score = self.socialcohesion

        hwbi /= total_wt
        outputs.hwbi = hwbi
        return outputs

