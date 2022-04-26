from odoo import http, _
from odoo.http import request


class Website(http.Controller):
    """Class for Website Controller."""

    @http.route('/login_page', type='http', auth='user', website=True)
    def login_page(self, **kw):
        return request.render('college_management.login_page', {})

    @http.route('/college', type='http', auth='user', website=True)
    def college(self, **kw):
        """Function to render form."""
        return request.render('college_management.create_form', {})

    @http.route('/college/webstudent', type='http', auth='user', website=True)
    def college_webstudent(self, **kw):
        """Function to get & store data in college_management.
        :return: record set"""
        request.env['college.management'].sudo().create(kw)
        college_list = request.env['college.management'].search([])
        return request.render('college_management.college_list', {
            'college_list': college_list
        })
