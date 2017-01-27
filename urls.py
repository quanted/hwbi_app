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

urlpatterns = [
    url(r'^$', description.description_page, {'model': "hwbi"}),
    url(r'^singlePage$', singlepage.singlePage, {'model': "hwbi"}),
    url(r'^input$', input.input_page, {'model': "hwbi"}),
    url(r'^map$', map.map_page, {'model': "hwbi"}),
    url(r'^algorithms$', algorithms.algorithm_page, {'model': "hwbi"}),
    url(r'^references$', references.references_page, {'model': "hwbi"}),
    url(r'^rest$', rest.rest_page, {'model': "hwbi"}),
    url(r'^test$', rest.rest_page_test, {'model': "hwbi"}),
    url(r'^swag$', views.getSwaggerJsonContent)
]

# 404 Error view (file not found)
handler404 = views.file_not_found
# 500 Error view (server error)
handler500 = views.file_not_found
# 403 Error view (forbidden)
handler403 = views.file_not_found