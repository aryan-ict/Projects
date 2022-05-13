from odoo import http, _
from odoo.http import request


class Website(http.Controller):
    """Class for Website Controller."""

    @http.route('/referral_hr', type='http', auth='user', website=True)
    def referral_program(self, **kw):
        """Function to render the form page,
        And to get values of Many2one field in frontend page."""
        referral_list = request.env['hr.employee'].search([])
        degree_list = request.env['hr.recruitment.degree'].search([])
        department_list = request.env['hr.job'].search([])
        return request.render('referral_program.hr_referral_program', {'referral_list': referral_list,
                                                                       'degree_list': degree_list,
                                                                       'department_list': department_list})

    @http.route('/referral_hr/thankyou', type='http', auth='user', website=True)
    def referral_program_thankyou(self, **kw):
        """Function to render Thank You page,
        And on the click of submit button entered values
        will be saved at the backend."""
        if kw:
            request.env['hr.referral.application'].sudo().create(kw)
        return request.render('referral_program.hr_referral_thankyou', {})

    @http.route('/referral_details', type='http', auth='user', website=True, csrf=False)
    def referral_details(self, **kw):
        """Function to render Records of Referral Program."""
        referral_details = request.env['hr.referral.application'].search([])
        return request.render('referral_program.referral_list', {'referral_detail': referral_details})
