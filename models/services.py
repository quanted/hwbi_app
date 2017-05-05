from django.db import models
from hwbi_outputs import ServiceOut

class Service(models.Model):
    """HWBI Service Model"""
    serviceID = models.TextField(max_length=3, primary_key=True)
    serviceTypeID = models.TextField(max_length=10)
    serviceName = models.TextField(max_length=50)
    serviceTypeName = models.TextField(max_length=10)
    description = models.TextField(max_length=50)
    name = models.TextField(max_length=50)
    min = models.FloatField
    max = models.FloatField
    score = 0.0

    def get_dict(self):
        dct = dict()
        dct['serviceID'] = self.serviceID
        dct['serviceTypeID'] = self.serviceTypeID
        dct['serviceName'] = self.serviceName
        dct['serviceTypeName'] = self.serviceTypeName
        dct['description'] = self.description
        dct['name'] = self.name
        dct['min'] = self.min
        dct['max'] = self.max
        dct['score'] = self.score
        return dct

    def __str__(self):
        return self.serviceID

    def get_service_out(self):
        service_out = ServiceOut()
        service_out.serviceID = self.serviceID
        service_out.name = self.name
        service_out.description = self.description
        service_out.serviceTypeName = self.serviceTypeName
        service_out.score = self.score
        return service_out

    def get_input_metadata(self):
        dct = {'name' : self.name, 'description' : self.description, 'value' : self.score}
        return dct


    class Meta:
        ordering = ('serviceID', 'serviceName')

