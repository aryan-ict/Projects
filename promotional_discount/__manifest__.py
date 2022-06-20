{
    'name': 'Promotional Discount',
    'summary': """Promotional Discount in sale order.""",
    'description': """
    This module will add promotional discount on the bases of records.
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
        'website'
    ],

    'data': [
        'security/ir.model.access.csv',
        'views/promotional_discount_views.xml'
    ],
}
