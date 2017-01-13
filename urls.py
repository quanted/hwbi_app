"""
Definition of urls for qed_hwbi.
"""

from datetime import datetime
from django.conf.urls import url
import django.contrib.auth.views


from hwbi_app import views
from hwbi_app import algorithms
from hwbi_app import description
from hwbi_app import input
from hwbi_app import links_left
from hwbi_app import map
from hwbi_app import references


urlpatterns = [
    url(r'^$', description.description_page, {'model': "hwbi"}),
    url(r'^/input$', input.input_page, {'model': "hwbi"}),
    url(r'^/map$', map.map_page, {'model': "hwbi"}),
    url(r'^/algorithms$', algorithms.algorithm_page, {'model': "hwbi"}),
    url(r'^/references$', references.references_page, {'model': "hwbi"}),

]