from django.db import models


class Domain(models.Model):
    """HWBI Domain Model"""
    domainID = models.TextField(max_length=10, primary_key=True)
    domainName = models.TextField(max_length=25, null=True, blank=True)
    name = models.TextField(max_length=20)
    min = models.IntegerField
    max = models.IntegerField

    def get_dict(self):
        dct = {}
#       dct['domainID'] = self.domainID
        dct['description'] = self.domainName
        dct['name'] = self.name
        dct['min'] = self.min
        dct['max'] = self.max
        dct['unit'] = 'domain score'
        dct['type'] = 'number'
        return dct
