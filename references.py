from django.template.loader import render_to_string
from django.http import HttpResponse
import importlib
import os
import links_left
from hwbi_app import views

def references_page(request, model='none', header='none'):
    #viewmodule = importlib.import_module('.views', 'models.' + model)
    header = views.header

    #text_file1 = open(os.path.join(os.environ['PROJECT_PATH'], 'models/' + model + '/' + model + '_references.html'),
    #                  'r')
    #x = text_file1.read()
    x = render_to_string('hwbi_references.html')
    html = render_to_string('01uberheader_main_drupal.html', {
        'SITE_SKIN': os.environ['SITE_SKIN'],
        'TITLE': header + ' References'})
    html += render_to_string('02uberintroblock_wmodellinks_drupal.html', {
        'CONTACT_URL': os.environ['CONTACT_URL'],
        'MODEL': model,
        'PAGE': 'algorithm'})
    html += render_to_string('04ubertext_start_index_drupal.html', {
        'TITLE': header + ' References',
        'TEXT_PARAGRAPH': x})
    html += render_to_string('04ubertext_end_drupal.html', {})
    html += links_left.ordered_list(model, 'references')
    html += render_to_string('06uberfooter.html', {})

    response = HttpResponse()
    response.write(html)
    return response
