from django.template.loader import render_to_string
from django.http import HttpResponse
# from django.shortcuts import redirect
# import os
# from django.conf import settings
# import links_left
# from hwbi_app import views



def singlePage(request, model='hwbi', header='none'):
    """ Returns the html of the references page for hwbi. """
    html = render_to_string('hwbi_singlepage.html', {})


    response = HttpResponse()
    response.write(html)
    return response