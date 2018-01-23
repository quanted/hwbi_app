import copy
import json


class HwbiOutputs:
    """HWBI Output"""

    def __init__(self):
        self.hwbi = 0.0
        self.statehwbi = 0.0
        self.nationhwbi = 52.7943325
        self.services = list()
        self.domains = list()

    def add_service(self, service):
        self.service.append(service)

    def add_domain(self, domain):
        self.domains.append(domain)

    def get_dict(self):
        dct = dict()
        dct['hwbi'] = self.hwbi
        dct['statehwbi'] = self.statehwbi
        dct['nationhwbi'] = self.nationhwbi
        lst_services = list()
        for service in self.services:
            lst_services.append(service.get_dict())
        lst_domains = list()
        for domain in self.domains:
            lst_domains.append(domain.get_dict())

        dct['services'] = lst_services
        dct['domains'] = lst_domains
        return dct


class ServiceOut:
    """HWBI ServiceOutput"""

    def __init__(self, serviceID='', name='', serviceTypeName='', description='', score=0.0):
        self.serviceID = serviceID
        self.name = name
        self.serviceTypeName = serviceTypeName
        self.description = description
        self.score = score

    def get_dict(self):
        return self.__dict__


class DomainOut:
    """HWBI Domain Output"""

    def __init__(self, domainID='', domainName='', description='', score=0.0, weight=0.0, stateScore=0.0, nationScore=0.0):
        self.domainID = domainID
        self.domainName = domainName
        self.description = description
        self.score = score
        self.weight = weight
        self.stateScore = stateScore
        self.nationScore = nationScore

    def reprJSON(self):
        return dict(domainID=self.domainID, domainName=self.domainName, description=self.description,
                    score=self.score, weight=self.weight, stateScore=self.stateScore, nationScore=self.nationScore)

    def get_dict(self):
        return self.__dict__


class ComplexEncoder(json.JSONEncoder):
    def default(self, obj):
        if hasattr(obj, 'reprJSON'):
            return obj.reprJSON()
        else:
            return json.JSONEncoder.default(self, obj)
