{
    'name': 'Contact Sale',
    'summary': """Sale Orders and history of Contacts""",
    'description': """
    This module contains history records of sale orders for customer.
    """,
    'version': '15.0.1.0.0',
    'category': 'Sales/Sales',
    'author': 'Aryan Modh',
    'website': 'http://www.aktivsoftware.com',
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',

    'depends': [
        'base',
        'sale_management',
        'contacts',
        'mail'
    ],

    'data': [
        'security/ir.model.access.csv',
        'data/sequence_data.xml',
        'views/res_partner.xml',
        'views/contact_sale_menu.xml',
        'views/contact_sale_views.xml',
    ],
}

