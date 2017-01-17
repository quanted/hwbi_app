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


def hwbi_map_page(request, model='hwbi', header='none'):

    # # If on public server, test user authentication
    # if settings.AUTH:
    #     if settings.MACHINE_ID == secret.MACHINE_ID_PUBLIC:
    #         if not request.user.is_authenticated():
    #             return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    #
    # header = views.header

    # html = render_to_string('01uberheader.html', {
    #     'site_skin': os.environ['SITE_SKIN'],
    #     'title': header + ' Inputs'})
    # html = html + render_to_string('hwbi/02uberintroblock_wmodellinks_hwbi.html', {
    #     'site_skin': os.environ['SITE_SKIN'],
    #     'model': model,
    #     'page': 'input'})
    # html = html + linksLeft.linksLeft()
    #
    # html = html + hwbiInputPage(request, model, header)
    #
    # html = html + render_to_string('06uberfooter.html', {'links': ''})

    # response = HttpResponse()
    # response.write(html)
    # return response

    html = render_to_string('04ubertext_start_index_drupal.html', {'TITLE': header})
    html += hwbi_map_page_html(request, model, header)
    html += render_to_string('04ubertext_end_drupal.html', {})

    return html


def hwbi_map_page_html(request, model, dummy):
    return render_to_string('hwbi_map_page.html', {})
