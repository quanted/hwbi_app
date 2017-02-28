"""
Definition of urls for qed_hwbi.
"""

from datetime import datetime
from django.conf.urls import url
import django.contrib.auth.views

import views
import algorithms
import description
import input
import links_left
import map
import references
import singlepage
import rest
import hwbi_rest

urlpatterns = [
    #url(r'^$', hwbi_rest, name='hwbi_rest'),

    url(r'^$', description.description_page, {'model': 'hwbi'}),
    url(r'^singlePage$', singlepage.singlePage, {'model': 'hwbi'}),
    url(r'^input$', input.input_page, {'model': 'hwbi'}),
    url(r'^map$', map.map_page, {'model': 'hwbi'}),
    url(r'^algorithms$', algorithms.algorithm_page, {'model': 'hwbi'}),
    url(r'^references$', references.references_page, {'model': 'hwbi'}),
    url(r'^api$', rest.rest_page, {'model': 'hwbi'}),
    url(r'^swag$', views.getSwaggerJsonContent),
    
    url(r'^rest$', hwbi_rest.get_hwbi),
       
    url(r'^rest/calc$', hwbi_rest.get_calc),
    url(r'^rest/calc/inputs$', hwbi_rest.get_calc_inputs),
    url(r'^rest/calc/outputs$', hwbi_rest.get_calc_outputs),
    url(r'^rest/calc/run$', hwbi_rest.get_calc_run),

    url(r'^rest/locations$', hwbi_rest.get_locations),
    url(r'^rest/locations/inputs$', hwbi_rest.get_locations_inputs),
    url(r'^rest/locations/outputs$', hwbi_rest.get_locations_outputs),
    url(r'^rest/locations/run$', hwbi_rest.get_locations_run)
  
]

# 404 Error view (file not found)
handler404 = views.file_not_found
# 500 Error view (server error)
handler500 = views.file_not_found
# 403 Error view (forbidden)
handler403 = views.file_not_found
