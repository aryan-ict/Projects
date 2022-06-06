{
    'name': "Bulk Products",
    'summary': """Bulk Products & Registration""",
    'description': """
Bulk Products & Registration
============================
Created to perform exam related tasks.""",

    'author': 'Aryan Modh',
    'website': 'https://www.aktivsoftware.com/',
    'category': 'Sales/Sales',
    'version': '15.0.1.0.0',
    'application': True,

    'depends': [
        'base',
        'sale_management',
        'website'
    ],

    'data': [
        'security/ir.model.access.csv',
        'views/sale_order_views.xml',
        'views/bulk_product_views.xml'
    ],

    "license": "LGPL-3"
}