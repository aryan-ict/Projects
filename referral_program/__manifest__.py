# -*- coding: utf-8 -*-
{
    'name': "Referral Program",
    'summary': """Referral Program & Registration""",
    'description': """
Referral Program & Registration
===============================
Created to perform Exam Practical tasks.""",
    'author': "Aryan Modh",
    'website': "https://www.aktivsoftware.com/",
    'category': 'Employee/Employee',
    'version': '15.0.1.0.0',
    # any module necessary for this one to work correctly
    'depends': [
        'base',
        'hr',
        'hr_recruitment',
        'website'
    ],
    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/hr_referral_application_views.xml',
        'views/referral_registration_front.xml'
    ],
    'application': True,
    'assets': {
        'web.assets_frontend': [
           'referral_program/static/src/css/referral.css'
        ],
    },
    "license": "LGPL-3"
    # only loaded in demonstration mode
}
