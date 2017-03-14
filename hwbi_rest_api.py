from django.http import HttpRequest, HttpResponse
import json
from django.core import serializers
import logging
from django.http import JsonResponse
import requests
import os
from datetime import datetime
from models.services import Service
from models.sqlite_mgr import get_services
from models.sqlite_mgr import get_domains
from models.meta_info import MetaInfo
from models.meta_info import Link
from models.meta_info import ComplexEncoder

version = 1.0

def get_hwbi(request):
    """
    HWBI Get hwbi
    """
    print('Inside get_hwbi')

    result = {}

    mi = MetaInfo()
    mi.description = 'The Human Well-Being Index (HWBI) was generated by researchers at the ' \
                     'U.S. Environmental Protection Agency using over one hundred ' \
                     'nationally-available data layers to assess economic, social, and ' \
                     'ecosystem services and calculate human well-being across the entire ' \
                     'U.S. at the regional, state, and county levels for years 2000-2010.'

    result['metaInfo'] = mi.get_dict()

    links = []
    link1 = Link('calc')
    links.append(link1.get_dict())
    link2 = Link('locations')
    links.append(link2.get_dict())
    link3 = Link('html')
    links.append(link3.get_dict())
    result['links'] = links

    response = HttpResponse()
    rslt = json.dumps(result, cls=ComplexEncoder)
    print(rslt)

    response.content = json.dumps(rslt)
    return response


def get_calc(request):
    """
    HWBI Get calc
    """
    print('Inside get_calc')

    result = {}

    mi = MetaInfo()
    mi.description = "The Human Well-Being Index (HWBI) model calculator (calc) " \
                     "uses 22 economic, ecosystem, and social services values to " \
                     "calculate eight 'domains of well-being': Connection to Nature, " \
                     "Cultural Fulfillment, Education, Health, Leisure Time, Living Standards, " \
                     "Safety & Security, and Social Cohesion. These domains of well-being " \
                     "are then weighed based on user-supplied 'relative importance values' " \
                     "and are used to determine the overall HWBI score."

    result['metaInfo'] = mi.get_dict()

    links = []
    link1 = Link('inputs','calc/inputs')
    links.append(link1.get_dict())
    link2 = Link('outputs', 'calc/outputs')
    links.append(link2.get_dict())
    link3 = Link('run', 'calc/run')
    links.append(link3.get_dict())
    link4 = Link('html', 'calc/hwbi')
    links.append(link4.get_dict())
    result['links'] = links

    response = HttpResponse()
    rslt = json.dumps(result, cls=ComplexEncoder)
    print(rslt)

    response.content = json.dumps(rslt)
    return response

def get_calc_inputs(request):
    """
    HWBI Get calc inputs
    """
    print('Inside get_calc_inputs')

    result = {}

    mi = MetaInfo()
    mi.description = "The Human Well-Being Index (HWBI) model calculator requires " \
                     "twenty-two economic; ecosystem; and social service values " \
                     "and a 'relative importance value' for each of the eight domains " \
                     "of well-being."

    result['metaInfo'] = mi.get_dict()
    result['metaInputs'] = get_services()
    links = []
    link1 = Link('inputs', 'calc/inputs')
    links.append(link1.get_dict())
    link2 = Link('outputs', 'calc/outputs')
    links.append(link2.get_dict())
    link3 = Link('run', 'calc/run')
    links.append(link3.get_dict())
    link4 = Link('html', 'calc/hwbi')
    links.append(link4.get_dict())
    result['links'] = links

    response = HttpResponse()
    rslt = json.dumps(result, cls=ComplexEncoder)
    print(rslt)

    response.content = json.dumps(rslt)
    return response


def get_calc_outputs(request):
    """
    HWBI Get calc outputs
    """
    print('Inside get_calc_outputs')

    result = {}

    mi = MetaInfo()
    mi.description = "The Human Well-Being Index (HWBI) model calculator provides " \
                     "eight 'domain of well-being' scores and an overall HWBI score."

    result['metaInfo'] = mi.get_dict()
    result['metaOutputs'] = get_domains()

    response = HttpResponse()
    rslt = json.dumps(result, cls=ComplexEncoder)
    print(rslt)

    response.content = json.dumps(rslt)
    return response


def get_calc_run(request):
    """
    HWBI Get Baseline Score by Location
    """

    data = None
    state = None
    county = None
    if request.method == 'POST':
        data = request.body
        state = data['state']
        county = data['county']

    response = HttpResponse()
    response.status_code = 500
    return response

def get_locations(request):
    """
    HWBI Get Baseline Score by Location
    """
    baseURL = os.getenv('HWBI_REST_SERVER')
    url = baseURL + '/rest/locations'
    return web_call_new(url)

def get_locations_inputs(request):
    """
    HWBI Get Baseline Score by Location
    """
    baseURL = os.getenv('HWBI_REST_SERVER')
    url = baseURL + '/rest/locations/inputs'
    return web_call_new(url)

def get_locations_outputs(request):
    """
    HWBI Get Baseline Score by Location
    """
    baseURL = os.getenv('HWBI_REST_SERVER')
    url = baseURL + '/rest/locations/outputs'
    return web_call_new(url)

def get_locations_run(request):
    """
    HWBI Get Baseline Score by Location
    """
    baseURL = os.getenv('HWBI_REST_SERVER')
    url = baseURL + '/rest/locations/run'
    data = None
    if request.method == 'POST':
        data = request.body
    return web_call_new(url, data)



def web_call_new(url, data=None):
	"""
	Makes the request to a specified URL
	and POST data. Returns resonse data as dict
	"""

	# TODO: Deal with errors more granularly... 403, 500, etc.
	try:
		if data == None:
			response = requests.get(url, timeout=10)
		else:
			response = requests.post(url, data=json.dumps(data), headers=headers, timeout=10)
		return json.loads(response.content)
	except requests.exceptions.RequestException as e:
		logging.warning("error at web call: {} /error".format(e))
		raise e