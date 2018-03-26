from django.db import models


class State(models.Model):
    """
    HWBI State Model
    """
    stateID = models.TextField(max_length=2, primary_key=True)
    state = models.TextField(max_length=50)
    score = models.FloatField
