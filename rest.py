from django.template.loader import render_to_string
from django.http import HttpResponse
from django.shortcuts import redirect
import os
from django.conf import settings
from django.shortcuts import render


# def rest_page(request, model='hwbi', header='none'):
#     header = views.header
#
#     x = render_to_string('hwbi_api.html')
#
#     """ Returns the html of the references page for hwbi. """
#     html = render_to_string('01epa_drupal_header.html', {})
#     html += render_to_string('02epa_drupal_header_bluestripe.html', {})
#     html += render_to_string('03epa_drupal_section_title.html', {})
#
#     html += render_to_string('04ubertext_start_index_drupal.html', {
#         'TITLE': header + ' REST API Documentation',
#         'TEXT_PARAGRAPH': x})
#
#     html += render_to_string('04ubertext_end_drupal.html', {})
#
#     html += render_to_string('10epa_drupal_footer.html', {})
#
#     response = HttpResponse()
#     response.write(html)
#     return response


def rest_page(request, model='hwbi', header='none'):
    return render(request, 'hwbi_api.html')