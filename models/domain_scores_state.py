from django.db import models

class DomainScoresState(models.Model):
    """HWBI Domain Model"""
    domainID = models.TextField(max_length=10, primary_key=True)
    geographicScale = models.TextField(max_length=25, null=True, blank=True)
    dataYear = models.TextField(max_length=20)
    score = models.FloatField
    stdError = models.FloatField
    GSS_Region = models.TextField(max_length=20)
    state = models.TextField(max_length=2)