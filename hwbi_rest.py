from django.http import HttpRequest, HttpResponse
import json
from django.conf import settings
import logging
import os


def getBaselineScoreByLocation(request):
    """
    HWBI Get Baseline Score by Location
    """