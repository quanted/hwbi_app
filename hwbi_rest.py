from django.http import HttpRequest, HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt
import logging
import os
import requests

def get_hwbi(request):
    """
    HWBI Get Baseline Score by Location
    """
    baseURL = os.getenv('HWBI_REST_SERVER')
    url = baseURL + '/rest/hwbi/'
    return web_call_new(url)


def get_calc(request):
    """
    HWBI Get Baseline Score by Location
    """
    baseURL = os.getenv('HWBI_REST_SERVER')
    url = baseURL + '/rest/hwbi/calc'
    return web_call_new(url)

def get_calc_inputs(request):
    """
    HWBI Get Baseline Score by Location
    """
    baseURL = os.getenv('HWBI_REST_SERVER')
    url = baseURL + '/rest/hwbi/calc/inputs'
    return web_call_new(url)

def get_calc_outputs(request):
    """
    HWBI Get Baseline Score by Location
    """
    baseURL = os.getenv('HWBI_REST_SERVER')
    url = baseURL + '/rest/hwbi/calc/outputs'
    return web_call_new(url)

def get_calc_run(request):
    """
    HWBI Get Baseline Score by Location
    """
    baseURL = os.getenv("HWBI_REST_SERVER")
    url = baseURL + '/rest/hwbi/calc/run'
    data = None
    if request.method == 'POST':
        data = request.body
    return web_call_new(url, data)

def get_locations(request):
    """
    HWBI Get Baseline Score by Location
    """
    baseURL = os.getenv('HWBI_REST_SERVER')
    url = baseURL + '/rest/hwbi/locations'
    return web_call_new(url)

def get_locations_inputs(request):
    """
    HWBI Get Baseline Score by Location
    """
    baseURL = os.getenv('HWBI_REST_SERVER')
    url = baseURL + '/rest/hwbi/locations/inputs'
    return web_call_new(url)

def get_locations_outputs(request):
    """
    HWBI Get Baseline Score by Location
    """
    baseURL = os.getenv('HWBI_REST_SERVER')
    url = baseURL + '/rest/hwbi/locations/outputs'
    return web_call_new(url)

def get_locations_run(request):
    """
    HWBI Get Baseline Score by Location
    """
    baseURL = os.getenv('HWBI_REST_SERVER')
    url = baseURL + '/rest/hwbi/locations/run'
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