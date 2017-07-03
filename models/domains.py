from django.db import models
from .hwbi_outputs import DomainOut


class Domain(models.Model):
    """HWBI Domain Model"""
    domainID = models.TextField(max_length=10, primary_key=True)
    domainName = models.TextField(max_length=25, null=True, blank=True)
    name = models.TextField(max_length=20)
    min = models.IntegerField
    max = models.IntegerField
    score = 0.0
    weight = 1.0

    def get_dict(self):
        dct = {}
        dct['domainID'] = self.domainID
        dct['description'] = self.domainName
        dct['domainName'] = self.name
        dct['min'] = self.min
        dct['max'] = self.max
        dct['unit'] = 'domain score'
        dct['type'] = 'number'
        dct['score'] = self.score
        dct['weight'] = self.weight
        return dct

    def get_domain_out(self):
        domain_out = DomainOut()
        domain_out.domainID = self.domainID
        domain_out.description = self.domainName
        domain_out.name = self.name
        domain_out.score = self.score
        domain_out.weight = self.weight
        return domain_out

    def get_input_metadata(self):
        dct = {'name' : self.name, 'description' : self.domainName, 'value' : self.weight}
        return dct

