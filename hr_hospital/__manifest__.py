# -*- coding: utf-8 -*-
{
    'name': "hr_hospital",
    'summary': '',

    'author': "My Company",
    'website': "http://www.yourcompany.com",


    'category': 'Customization',
    'license': 'OPL-1',
    'version': '15.0.1.0.0',


    'depends': ['base_setup'],
    'external_dependencies': {'python': [], },

    'data': [
        'security/ir.model.access.csv',

        'views/hr_hospital_menu.xml',
        'views/patient_view.xml',
        'views/doctor_view.xml',



    ],

    'demo': [],

    'installable': True,
    'auto_install': False,

    'images': [
        'static/description/icon.png',
    ],

    'price': 0,
    'currency': 'USD',

}
