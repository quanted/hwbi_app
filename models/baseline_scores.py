from django.db import models
from .hwbi_outputs import ServiceOut

class BaselineScore(models.Model):
    """HWBI BaselineScore Model"""
    county_FIPS = models.TextField(max_length=5, primary_key=True)
    stateID = models.TextField(max_length=2)
    state = models.TextField(max_length=20)
    county = models.TextField(max_length=30)
    serviceID = models.TextField(max_length=3)
    serviceName = models.TextField(max_length=10)
    serviceTypeName = models.TextField(max_length=10)
    score = models.FloatField
    description = models.TextField(max_length=50)
    serviceType = models.TextField(max_length=15)
    name = models.TextField(max_length=15)

    def get_dict(self):
        dct = {}
        dct['county_FIPS'] = self.county_FIPS
        dct['stateID'] = self.stateID
        dct['state'] = self.state
        dct['county'] = self.county
        dct['serviceID'] = self.serviceID
        dct['serviceName'] = self.serviceName
        dct['score'] = self.score
        dct['description'] = self.description
        dct['serviceType'] = self.serviceType
        dct['name'] = self.name
        return dct

    def __str__(self):
        return self.serviceID

    def get_service_out(self):
        service_out = ServiceOut()
        service_out.serviceID = self.serviceID
        service_out.name = self.name
        service_out.serviceTypeName = self.serviceTypeName
        service_out.score = self.score
        service_out.description = self.description
        return service_out


    class Meta:
        ordering = ('state', 'county', 'serviceID')