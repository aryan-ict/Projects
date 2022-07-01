{
    'name': 'Covid Delivery Message',
    'summary': """Covid Message in Shop.""",
    'description': """
    On checking Boolean field in Config Settings of website,
    It will show Attention Message.
    """,
    'version': '15.0.1.0.0',
    'category': 'Website/Website',
    'author': 'Aryan Modh',
    'website': 'http://www.aktivsoftware.com',
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',

    'depends': [
        'base',
        'website',
        'website_sale'
    ],

    'data': [
        'security/security.xml',
        'views/shop_covid_warning_frontend.xml',
        'views/res_config_settings_views.xml',
    ],
}
