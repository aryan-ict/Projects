from odoo import http, _
from odoo.http import request


class Website(http.Controller):
    """Class for Website Controller."""

    @http.route('/college', type='http', auth='public', website=True)
    def college(self, **kw):
        """Function to get data from college_management.
        :return: record set"""
        return request.render('college_management.create_form', {})

    @http.route('/college/webstudent', type='http', auth='public', website=True)
    def college_webstudent(self, **kw):
        request.env['college.management'].sudo().create(kw)
        college_list = request.env['college.management'].search([])
        return request.render('college_management.college_list', {
            'college_list': college_list
        })

    # @http.route('/college/list', type='http', auth='public', website=True)
    # def college_list(self, **kw):

