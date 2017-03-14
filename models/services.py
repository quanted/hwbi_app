from django.db import models

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

    def get_dict(self):
        dct = {}
        dct['serviceID'] = self.serviceID
        dct['serviceTypeID'] = self.serviceTypeID
        dct['serviceName'] = self.serviceName
        dct['serviceTypeName'] = self.serviceTypeName
        dct['description'] = self.description
        dct['name'] = self.name
        dct['min'] = self.min
        dct['max'] = self.max
        return dct

    def __str__(self):
        return self.serviceID

    class Meta:
        ordering = ('serviceID', 'serviceName')