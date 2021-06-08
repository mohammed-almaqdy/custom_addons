# -*- coding: utf-8 -*-
{
    'name': "costum_events",

    'summary': """
    this assigiment for orginize the events and git more information about the orgnizers
        """,

    'description': """
    in this assigment you can booking for your events or celeberate
    and chose the orginizers and the equepment for your event easly 
    just enter in our website and git your wishes things for your 
    event 
    have good event
    """,

    'author': "Mohammed al-maqdy",
    
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['event'],

    'data': [
        'security/ir.model.access.csv',
        'views/myevents.xml',
        'views/organizer.xml',
        'views/materials.xml',
    ],
    
    'demo': [
        'demo/demo.xml',
    ],
}
