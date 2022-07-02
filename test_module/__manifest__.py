{
    'name': "AutoUpdate Sale Order Line",
    'summary': """AutoUpdate Sale Order Line""",
    'description': """
    Add Product M2o and Qty in sale.order. onchange of Product and Qty, Order line
    should be generated (If we select the same Product twice, we just need to update its
    ordered qty. There will be only one product line on Sales Line)
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
        'account'
    ],

    'data': [
        'views/sale_order_views.xml',
        'views/product_product_views.xml',
        'views/account_move_line_views.xml',
        'reports/sale_order_report_inherit.xml'
    ],

    "license": "LGPL-3"
}
