"""
Definition of urls for qed_hwbi.
"""

from datetime import datetime
from django.conf.urls import url
import django.contrib.auth.views

from . import views, algorithms, description, input, links_left, map
from . import references, singlepage, rest, hwbi_rest_api

# Django 2.0 url import
from django.urls import path

from django.contrib import admin
from .disc_views import HWBI as hwbi
from . import disc_rest_api as disc_api

# if settings.IS_PUBLIC:
urlpatterns = [
    # HWBI Django 1.11 urls
    # front end urls
    # url(r'^$', description.description_page, {'model': 'hwbi'}),
    # url(r'^singlePage$', singlepage.singlePage, {'model': 'hwbi'}),
    # url(r'^input$', input.input_page, {'model': 'hwbi'}),
    # url(r'^map$', map.map_page, {'model': 'hwbi'}),
    # url(r'^algorithms$', algorithms.algorithm_page, {'model': 'hwbi'}),
    # url(r'^references$', references.references_page, {'model': 'hwbi'}),
    # url(r'^rest$', rest.rest_page, {'model': 'hwbi'}),
    # url(r'^rest/swag$', views.getSwaggerJsonContent),

    # rest urls
    # url(r'^rest$', hwbi_rest_api.get_hwbi),

    # url(r'^rest/calc$', hwbi_rest_api.get_calc),
    # url(r'^rest/calc/inputs$', hwbi_rest_api.get_calc_inputs),
    # url(r'^rest/calc/outputs$', hwbi_rest_api.get_calc_outputs),
    # url(r'^rest/calc/run$', hwbi_rest_api.get_calc_run),

    # url(r'^rest/locations$', hwbi_rest_api.get_locations),
    # url(r'^rest/locations/inputs$', hwbi_rest_api.get_locations_inputs),
    # url(r'^rest/locations/outputs$', hwbi_rest_api.get_locations_outputs),
    # url(r'^rest/locations/run$', hwbi_rest_api.get_locations_run)

    # HBWI Django 2.0 urls
    path("", description.description_page, {'model': 'hwbi'}),
    path("singlePages/", singlepage.singlePage, {'model': 'hwbi'}),
    path("input/", input.input_page, {'model': 'hwbi'}),
    path('map/', map.map_page, {'model': 'hwbi'}),
    path('algorithms/', algorithms.algorithm_page, {'model': 'hwbi'}),
    path('references/', references.references_page, {'model': 'hwbi'}),
    path('rest/', rest.rest_page, {'model': 'hwbi'}),
    path('rest/swag/', views.getSwaggerJsonContent),

    path('rest/', hwbi_rest_api.get_hwbi),

    path('rest/calc/', hwbi_rest_api.get_calc),
    path('rest/calc/inputs/', hwbi_rest_api.get_calc_inputs),
    path('rest/calc/outputs/', hwbi_rest_api.get_calc_outputs),
    path('rest/calc/run/', hwbi_rest_api.get_calc_run),

    path('rest/locations/', hwbi_rest_api.get_locations),
    path('rest/locations/inputs/', hwbi_rest_api.get_locations_inputs),
    path('rest/locations/outputs/', hwbi_rest_api.get_locations_outputs),
    path('rest/locations/run/', hwbi_rest_api.get_locations_run),

    # Django 2.0 syntax url dispatcher HWBI DISC
    # path('', hwbi.disc_page),
    path('admin/', admin.site.urls),
    path('disc/', hwbi.disc_page),
    path('disc/<slug:page>/', hwbi.disc_page),
    path('disc/community-snapshot/', hwbi.disc_page, {'page': 'community-snapshot'}),
    path('disc-alt/', hwbi.get_disc_alt_page),

    # HWBI DISC rest api endpoints
    path('disc/rest/scores', disc_api.get_disc_scores)

    # Django 1.11 syntax url dispatcher HWBI DISC
    # url(r'^$', hwbi.disc_page),
    # url(r'^admin/$', admin.site.urls),
    # url(r'^disc/$', hwbi.disc_page),
    # HWBI DISC rest api endpoints
    # url(r'^disc/rest/scores', disc_api.get_disc_scores),
    # url(r'^disc/(?P<page>.+)$', hwbi.disc_page),

]
# else:
#     urlpatterns = [
#         url(r'^$', views.hwbi_landing_page),
#     ]


# 404 Error view (file not found)
handler404 = views.file_not_found
# 500 Error view (server error)
handler500 = views.file_not_found
# 403 Error view (forbidden)
handler403 = views.file_not_found
