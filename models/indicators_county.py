from django.db import models


class IndicatorsCounty(models.Model):
    """
    HWBI Indicator County Model
    """
    county_FIPS = models.TextField(max_length=5, primary_key=True)
    stateID = models.TextField(max_length=2)
    state = models.TextField(max_length=20)
    county = models.TextField(max_length=30)
    indicator = models.TextField(max_length=100)
    score = models.FloatField

    def get_dict(self):
        dct = {}
        dct['stateID'] = self.stateID
        dct['county'] = self.county
        dct['score'] = self.score
        dct['indicator'] = self.indicator
        return dct
