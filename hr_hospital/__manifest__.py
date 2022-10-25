# -*- coding: utf-8 -*-
{
    'name': "hr_hospital",
    'summary': '',

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Customization',
    'license': 'OPL-1',
    'version': '15.0.1.0.0',

    # any module necessary for this one to work correctly
    'depends': [],
    'external_dependencies': {'python': [], },
    # always loaded
    'data': [
        'security/ir.model.access.csv',

        'views/menu.xml',
        'views/patient.xml',
    ],
    # only loaded in demonstration mode
    'demo': [],

    'installable': True,
    'auto_install': False,

    'images': [
        'static/description/cover.png',
        'static/description/icon.png',
    ],

    'price': 0,
    'currency': 'USD',

}