"""
module: HWBI
views.py
"""

from django.http import HttpResponse
from django.template.loader import render_to_string
import json


class HWBI:
    header = 'HWBI'

    def disc_page(self, page=''):
        if page is '':
            page = 'about'
        location = {}
        for key, value in self.POST.dict().items():
            location[key] = str(value)
        html = build_disc_page(location, page=page)
        response = HttpResponse()
        response.write(html)
        return response


def build_disc_page(loc, page):
    imports, body = get_page_html(loc, page)

    # EPA drupal page template
    html = render_to_string('disc/drupal_2017/01epa_drupal_header.html', {})
    html += render_to_string('disc/drupal_2017/02epa_drupal_header_bluestripe.html', {})

    # CUSTOM CSS IMPORT
    html += imports

    html += render_to_string('disc/drupal_2017/03epa_drupal_section_title_generic.html', {
        'HEADER': 'Well-Being and Your Community'
    })

    # Soft intro
    if page == 'about':
        html += render_to_string('disc/hwbi-disc_intro.html')

    menu_pages = set_menu(page)
    # Quick Menu
    html += render_to_string('disc/hwbi-disc_quick_menu.html', {
        'ABOUT': menu_pages['about'],
        'COMMUNITY_SNAPSHOT': menu_pages['community-snapshot'],
        'CUSTOMIZE': menu_pages['customize'],
        'ADDITIONAL_RESOURCES': menu_pages['additional-resources']
    })

    # HWBI page specific body
    html += body
    html += render_to_string('disc/drupal_2017/10epa_drupal_footer.html', {})
    return html


def set_menu(page):
    q_menu = {'about': '', 'community-snapshot': '', 'customize': '', 'additional-resources': ''}

    if page in q_menu.keys():
        q_menu[page] = 'menu_border_focus'

    if page == 'community-snapshot':
        q_menu['about'] = 'menu_border_left'
        q_menu['customize'] = 'menu_border_right'
        q_menu['additional-resources'] = 'menu_border_right'
    elif page == 'customize':
        q_menu['about'] = 'menu_border_left'
        q_menu['community-snapshot'] = 'menu_border_left'
        q_menu['additional-resources'] = 'menu_border_right'
    elif page == 'additional-resources':
        q_menu['about'] = 'menu_border_left'
        q_menu['community-snapshot'] = 'menu_border_left'
        q_menu['customize'] = 'menu_border_left'
    else:
        q_menu['about'] = 'menu_border_focus'
        q_menu['community-snapshot'] = 'menu_border_right'
        q_menu['customize'] = 'menu_border_right'
        q_menu['additional-resources'] = 'menu_border_right'

    return q_menu


def get_page_html(location, page):
    temp_google_key = 'AIzaSyDEC5r_Tq31qfF8BKIdhUAH1KorOfjLV4g'
    loc_obj = {}
    if 'location_value' in location:
        loc_obj = json.loads(location['location_value'])

    # HWBI page specifics
    if page == 'about':
        imports = render_to_string('disc/hwbi-disc_about-imports.html', {'API_KEY': temp_google_key})
        body = render_to_string('disc/hwbi-disc_about.html')
    elif page == 'community-snapshot':
        imports = render_to_string('disc/hwbi-disc_snapshot-imports.html', {'API_KEY': temp_google_key})
        body = render_to_string('disc/hwbi-disc_snapshot-search-field.html', {'LOCATION': json.dumps(loc_obj)})
        body += render_to_string('disc/hwbi-disc_snapshot-body.html')
    elif page == 'customize':
        imports = render_to_string('disc/hwbi-disc_customize-imports.html', {'API_KEY': temp_google_key})
        body = render_to_string('disc/hwbi-disc_customize-body.html', {'LOCATION': json.dumps(loc_obj)})
    else:
        imports = render_to_string('disc/hwbi-disc_general-imports.html', {'API_KEY': temp_google_key})
        body = render_to_string('disc/hwbi-disc_search-field.html', {'LOCATION': json.dumps(loc_obj)})
    return imports, body
