# -*- coding: utf-8 -*-
{
    'name': "NGO_p",

    'summary': """
        This Module is for Orphans Management""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # for the full list
    'category': 'Custom',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','contacts'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',

        'views/res_partner.xml',
        'views/orphan_organization.xml',
        'views/orphan_request.xml',
        'views/orphan_members.xml',
        'views/orphan_organization_expenses.xml',
        'views/expense_type.xml',
        'views/orphan_organization_donation.xml',
        'views/main_menu.xml',
        'views/organization_advertise.xml',

        'reports/doner_paper_format.xml',
        'reports/donation_paper_format.xml',
        'reports/template.xml',
        'reports/donation_details_templates.xml',
        'reports/expense_template.xml',
        'reports/receipt_report.xml',
        'reports/expense_report.xml',
    ],
    # only loaded in demonstration mode
    'license': 'LGPL-3',
}
