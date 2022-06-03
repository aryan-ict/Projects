{
    'name': 'Batch Sale',
    'summary': """Sale Orders and Batch of sale.""",
    'description': """
    This module contains workflow of Batch Sale.
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
        'mail',
        'website'
    ],

    'data': [
        'security/ir.model.access.csv',
        'data/sequence_data.xml',
        'views/batch_sale_workflow_menu.xml',
        'views/batch_sale_workflow_views.xml',
        'views/contact_form_frontend.xml'
    ],

    'assets': {
        'web.assets_frontend': [
            'aryanmodh_02062022/static/src/css/contact_form.css'
        ],
    },
}
