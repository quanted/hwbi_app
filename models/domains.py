from django.db import models


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
