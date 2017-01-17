"""
.. module:: hwbi_input
   :synopsis: A useful module indeed.
"""
import os
from django.http import HttpResponse
from django.shortcuts import redirect
from django.template.loader import render_to_string
from django.conf import settings
from hwbi_app import views
from hwbi_app import links_left

def hwbi_input_page(request, model='hwbi', header='none'):
    html = render_to_string('04ubertext_start_index_drupal.html', {'TITLE': header})
    html += hwbi_input_page_html(request, model, header)
    html += render_to_string('04ubertext_end_drupal.html', {})
    return html

def hwbi_input_page_html(request, model, dummy):
    return render_to_string('hwbi_input_page.html', {})
