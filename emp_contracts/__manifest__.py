{
    'name': "Employee Contracts(Task)",
    'summary': """Employee Contracts""",
    'description': """
Employee Contracts
============================
Created to perform Assigned tasks.""",

    'author': 'Aryan Modh',
    'website': 'https://www.aktivsoftware.com/',
    'category': 'Human Resource/Employee',
    'version': '15.0.1.0.0',
    'application': True,

    'depends': [
        'base',
        'hr',
        'website'
    ],

    'data': [
        'views/emp_contracts_portal.xml',
    ],

    "license": "LGPL-3"
}
