{
    'name': "New Order Line",
    'summary': """New Order Line""",
    'description': """
   On selection of sale order line
   it will automatically add lines in New Order Line.
   """,

    'author': 'Aryan Modh',
    'website': 'https://www.aktivsoftware.com/',
    'category': 'Sales/Sales',
    'version': '15.0.1.0.0',
    'application': True,
    'auto_install': False,

    'depends': [
        'base',
        'sale_management',
    ],

    'data': [
        'security/ir.model.access.csv',
        'views/sale_order_views.xml'
    ],

    "license": "LGPL-3"
}