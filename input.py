from django.template.loader import render_to_string
from django.http import HttpResponse
from django.shortcuts import redirect
import os
from django.conf import settings
import links_left
from hwbi_app import views



def input_page(request, model='hwbi', header='none'):
    header = views.header
    x = render_to_string('hwbi_input_page.html')

    """ Returns the html of the references page for hwbi. """
    html = render_to_string('01epa_drupal_header.html', {})
    html += render_to_string('02epa_drupal_header_bluestripe_onesidebar.html', {})
    html += render_to_string('03epa_drupal_section_title.html', {})

    html += render_to_string('04ubertext_start_index_drupal.html', {
        'TEXT_PARAGRAPH': x})

    html += render_to_string('04ubertext_end_drupal.html', {})

    html += links_left.ordered_list(model, 'run_model')
    html += render_to_string('10epa_drupal_footer.html', {})


    response = HttpResponse()
    response.write(html)
    return response







# import os
# from django.template.loader import render_to_string
# from django.http import HttpResponse, HttpResponseRedirect
# from django.conf import settings
# from django.shortcuts import redirect
# import importlib
# import links_left
# from hwbi_app import views
# from hwbi_app import links_left
#
#
#
#
# def hwbi_input_page(request, model='hwbi', header='none'):
#     html = render_to_string('04ubertext_start_index_drupal.html', {'TITLE': header})
#     html += hwbi_input_page_html(request, model, header)
#     html += render_to_string('04ubertext_end_drupal.html', {})
#     return html
#
#
# def hwbi_input_page_html(request, model, dummy):
#     return render_to_string('hwbi_input_page.html', {})
#
#
# def input_page(request, model='none', header='none'):
#
#     header = views.header
#
#     html = render_to_string('01uberheader_main_drupal.html', {
#         'SITE_SKIN': os.environ['SITE_SKIN'],
#         'TITLE': header})
#     html += render_to_string('02uberintroblock_wmodellinks_drupal.html', {
#         'CONTACT_URL': os.environ['CONTACT_URL'],
#         'MODEL': model,
#         'PAGE': 'input'})
#
#
#     html += hwbi_input_page(request,model, header)
#
#     html += links_left.ordered_list(model, 'run_model')
#     html += render_to_string('06uberfooter.html', {})
#
#     response = HttpResponse()
#     response.write(html)
#     return response