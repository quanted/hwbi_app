import copy
from scores import Scores
from domain_weights import DomainWeights

class HWBICalc:
    """HWBI Scores Model"""
    def __init__(self):
        self.domain_weights = None
        self.scores = None
        self.scaled_scores = None
        self.connectiontonature = 0.0
        self.culturalfulfillment = 0.0
        self.education = 0.0
        self.health = 0.0
        self.leisuretime = 0.0
        self.livingstandards = 0.0
        self.safetyandsecurity = 0.0
        self.socialcohesion = 0.0

    def calc(self, scores, domain_weights):
    #Have to divide these guys by 100
        self.scores = copy.deepcopy(scores)
        self.scaled_scores = copy.deepcopy(scores)

        self.domain_weights = copy.deepcopy(domain_weights)

        #Divide scores by 100 for calc purposes
        for attr, value in self.scaled_scores.__dict__.iteritems():
            val = self.scaled_scores.__dict__[attr]
            self.scaled_scores.__dict__[attr] = val / 100

        #Sum up the total for all the weights
        total_wt = 0.0
        for attr, value in self.domain_weights.__dict__.iteritems():
            val = self.domain_weights.__dict__[attr]
            total_wt += val

        try:

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
        hwbi += self.connectiontonature * self.domain_weights.connectiontonature
        hwbi += self.culturalfulfillment * self.domain_weights.culturalfulfillment
        hwbi += self.education * self.domain_weights.education

        hwbi += self.health * self.domain_weights.health
        hwbi += self.leisuretime * self.domain_weights.leisuretime
        hwbi += self.livingstandards * self.domain_weights.livingstandards

        hwbi += self.safetyandsecurity * self.domain_weights.safetyandsecurity
        hwbi += self.socialcohesion * self.domain_weights.socialcohesion

        hwbi /= total_wt

        return hwbi

