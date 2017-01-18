import os
from django.template.loader import render_to_string
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
from django.shortcuts import redirect
import importlib
from hwbi_app import views



def hwbi_singlepage(request, model='hwbi', header='none'):
    html = render_to_string('04ubertext_start_index_drupal.html', {'TITLE': header})
    html += hwbi_singlepage_html(request, model, header)
    html += render_to_string('04ubertext_end_drupal.html', {})
    return html


def hwbi_singlepage_html(request, model, dummy):
    return render_to_string('hwbi_singlepage.html', {})


def singlePage(request, model='none', header='none'):

    header = views.header

    html = render_to_string('01epa_drupal_header.html', {
        'SITE_SKIN': os.environ['SITE_SKIN'],
        'TITLE': header})
    html += render_to_string('02uberintroblock_wmodellinks_drupal.html', {
        'CONTACT_URL': os.environ['CONTACT_URL'],
        'MODEL': model,
        'PAGE': 'input'})


    html += hwbi_singlepage(request, model, header)

    html += render_to_string('10epa_drupal_footer.html', {})
    
    response = HttpResponse()
    response.write(html)
    return response