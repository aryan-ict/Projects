{
    'name': 'Credit Limit',
    'summary': """Credit Limit & Block Limit.""",
    'description': """
    This module will be used to apply credit limit and block limit.
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
        'mail',
        'contacts'
    ],

    'data': [
        'security/ir.model.access.csv',
        'views/res_partner_views.xml',
        'views/credit_limit_views.xml',
    ],
}
