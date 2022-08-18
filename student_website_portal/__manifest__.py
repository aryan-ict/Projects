{
    'name': "Student Website Portal",
    'summary': """Student Website Portal""",
    'description': """
   Will Add custom portal in My account menu
   of My Student.
   """,

    'author': 'Aryan Modh',
    'website': 'https://www.aktivsoftware.com/',
    'category': 'Website/Website',
    'version': '15.0.1.0.0',
    'application': True,
    'auto_install': False,
    "license": "LGPL-3",

    'depends': [
        'base',
        'website',
    ],

    'data': [
        'security/ir.model.access.csv',
        'views/student_website_portal_views.xml',
        'views/student_website_portal_template.xml'
    ],
    'assets': {
        'web.assets_frontend': [
            'student_website_portal/static/src/js/create_edit_data.js',
            'student_website_portal/static/src/css/student_create_form.css',
        ],
    }

}
