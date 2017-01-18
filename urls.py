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

urlpatterns = [
    url(r'^$', description.description_page, {'model': "hwbi"}),
    url(r'^singlePage$', singlepage.singlePage, {'model': "hwbi"}),
    url(r'^input$', input.input_page, {'model': "hwbi"}),
    url(r'^map$', map.map_page, {'model': "hwbi"}),
    url(r'^algorithms$', algorithms.algorithm_page, {'model': "hwbi"}),
    url(r'^references$', references.references_page, {'model': "hwbi"}),
]
