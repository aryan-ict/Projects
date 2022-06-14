{
    'name': "Subscription Lines",
    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",
    'description': """
        Long description of module's purpose
    """,
    'author': "My Company",
    'website': "http://www.yourcompany.com",
    'category': 'Accounting/Accounting',
    'version': '15.0.1.0.0',
    'application': True,

    # any module necessary for this one to work correctly
    'depends': [
        'base',
        'account'
    ],
    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/subscriptions_lines_menu.xml',
        'views/subscriptions_lines_view.xml',
        'views/account_move_line_view.xml',
        'views/res_partner.xml'
    ],
    "license": "LGPL-3"
    # only loaded in demonstration mode
}
# -*- coding: utf-8 -*-
