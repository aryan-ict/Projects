# -*- coding: utf-8 -*-
{
    'name': "College Management",
    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",
    'description': """
        Long description of module's purpose
    """,
    'author': "My Company",
    'website': "http://www.yourcompany.com",
    'category': 'Uncategorized',
    'version': '15.0.0.1.2',
    'depends': [
        'base',
        'mail',
        'hr',
        'website',
        'portal',
        'contacts'
    ],
    'data': [
        'security/ir.model.access.csv',
        'data/mail_template.xml',
        # 'wizard/wizard_views.xml',
        'views/views.xm l',
        # 'views/website_form.xml',
        # 'views/login_page.xml'
        # 'views/student_views.xml',
    ],
    # 'assets': {
    #     'web.assets_frontend': [
    #         'college_management/static/src/css/college_form.css',
    #         'college_management/static/src/css/login_page.css'
    #     ],
    # },
    "license": "LGPL-3"
    # only loaded in demonstration mode
}
