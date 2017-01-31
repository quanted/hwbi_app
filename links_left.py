from django.template.loader import render_to_string
from collections import OrderedDict
from django.shortcuts import redirect


# 03ubertext_links_left:
def ordered_list(model=None, page=None):
    link_dict = OrderedDict([
        ('Model', OrderedDict([
                ('HWBI', 'hwbi'),
            ])
        ),
        ('Documentation', OrderedDict([
                ('API Documentation', '/qedinternal.epa.gov/hwbi/rest'),
                ('Source Code', '/github.com/USEPA/HWBI')
            ])
        )
    ])

    #return render_to_string('hwbi/03ubertext_links_left_drupal.html', {
    return render_to_string('03hwbi_links_left_drupal.html', {
        'LINK_DICT': link_dict,
        'MODEL': model,
        'PAGE': page
    })