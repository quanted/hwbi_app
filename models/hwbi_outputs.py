import copy
import json


class HwbiOutputs:
    """HWBI Output"""

    def __init__(self):
        self.hwbi = 0.0
        self.scores = list()
        self.domains = list()

    def add_score(self, score):
        self.scores.append(score)

    def add_domain(self, domain):
        self.domains.append(domain)

    def get_dict(self):
        dct = dict()
        dct['hwbi'] = self.hwbi
        lst_scores = list()
        for score in self.scores:
            lst_scores.append(score.get_dict())
        lst_domains = list()
        for domain in self.domains:
            lst_domains.append(domain.get_dict())

        dct['services'] = lst_scores
        dct['domains'] = lst_domains
        return dct


class ScoreOut:
    """HWBI ServiceOutput"""

    def __init__(self, serviceID='', name='', serviceType='', description='', score=0.0):
        self.serviceID = serviceID
        self.name = name
        self.serviceType = serviceType
        self.description = description
        self.score = score

    def get_dict(self):
        return self.__dict__


class DomainOut:
    """HWBI Domain Output"""

    def __init__(self, domainID='', domainName='', description='', score=0.0, weight=0.0):
        self.domainID = domainID
        self.domainName = domainName
        self.description = description
        self.score = score
        self.weight = weight

    def reprJSON(self):
        return dict(domainID=self.domainID, domainName=self.domainName, description=self.description, score=self.score, weight=self.weight)

    def get_dict(self):
        return self.__dict__


class ComplexEncoder(json.JSONEncoder):
    def default(self, obj):
        if hasattr(obj, 'reprJSON'):
            return obj.reprJSON()
        else:
            return json.JSONEncoder.default(self, obj)
