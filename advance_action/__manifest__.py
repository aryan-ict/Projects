# -*- coding: utf-8 -*-

{
    'name': "Advance Action",
    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",
    'description': """
        Long description of module's purpose
    """,
    'author': "My Company",
    'website': "http://www.yourcompany.com",
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',
    # any module necessary for this one to work correctly
    'depends': [
        'base',
        'contacts',
        'sale_management',
        'hr'
    ],
    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'data/sale_order_cron.xml',
        'wizard/timesheet_wizard_view.xml',
        'views/advance_action_views.xml',
        'views/res_partner_views.xml',
        'views/contacts_list.xml',
        'views/hr_employee_views.xml'

    ],
    "license": "LGPL-3"
    # only loaded in demonstration mode
}
