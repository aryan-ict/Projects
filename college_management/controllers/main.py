from odoo import http, _
from odoo.http import request
from odoo.addons.portal.controllers import portal


class Website(http.Controller):
    """Class for Website Controller."""

    @http.route('/login_page', type='http', auth='user', website=True)
    def login_page(self, **kw):
        return request.render('college_management.login_page', {})

    @http.route('/college', type='http', auth='user', website=True)
    def college(self, **kw):
        """Function to render form."""
        customer_list = request.env['res.partner'].sudo().search([])
        return request.render('college_management.create_form', {'partner': customer_list})

    @http.route('/college/webstudent', type='http', auth='user', website=True)
    def college_webstudent(self, **kw):
        """Function to get & store data in college_management.
        :return: record set"""
        if kw:
            request.env['college.management'].sudo().create(kw)
        college_list = request.env['college.management'].search([])
        return request.render('college_management.college_list', {
            'college_list': college_list
        })


class CollegeCustomerPortal(portal.CustomerPortal):
    def _prepare_home_portal_values(self, counters):
        values = super(CollegeCustomerPortal, self)._prepare_home_portal_values(counters)
        student_count = request.env["college.management"].search_count([])
        values.update({
            'student_count': student_count
        })
        return values
