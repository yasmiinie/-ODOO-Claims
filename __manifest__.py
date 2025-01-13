# -*- coding: utf-8 -*-
{
    'name': "Claims",

    'summary': """Gestion des réclamations""",

    'description': """
        Gestion des réclamations module pour :
            - Recensement des réclamations
            - Traitement des réclamations
            - Communication avec le réclamant           
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Test',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'templates.xml',
        'views/clientspec.xml',
	    'reports.xml',
    ],

    # only loaded in demonstration mode
    'demo': [
        'demo.xml',
    ],
}