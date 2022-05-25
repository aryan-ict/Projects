from odoo import http, _
from odoo.http import request
from odoo.addons.portal.controllers import portal
import base64


class EmployeePortal(portal.CustomerPortal):
    def _prepare_home_portal_values(self, counters):
        """Function to get counts of records in Portal Menu
        of Contracts."""
        values = super(EmployeePortal, self)._prepare_home_portal_values(counters)
        contract_count = request.env["hr.contract"].search_count(
            [('employee_id', '=', request.env.user.employee_id.id)])
        values.update({
            'contract_count': contract_count
        })
        return values

    @http.route('/my/contracts', type='http', auth='user', website=True, csrf=False)
    def login_page(self, **kw):
        """Function to render the list template on the
        click of Contract portal."""
        contracts_list = request.env['hr.contract'].search([('employee_id', '=', request.env.user.employee_id.id)])
        return request.render('emp_contracts.portal_my_contracts', {
            'contracts_list': contracts_list
        })

    @http.route(['/my/contracts/details/<model("hr.contract"):contracts_list>'], type='http', auth='user', website=True)
    def contracts_details(self, contracts_list):
        """Function to render the details template and
        to link templates."""
        return request.render("emp_contracts.contracts_detail", {
            'details': contracts_list
        })

    @http.route('/contract/upload', type='http', auth='user', website=True)
    def upload_files(self, **post):
        attached_files = request.httprequest.files.getlist('attachment')
        project_id = post.get('project_id')
        print("=========================", project_id)
        for attachment in attached_files:
            print("==========================", post)
            contract = request.env['hr.contract'].browse(post.get('project_id'))
            print("========================", contract)
            print("----------------------------", attachment)
            file = post.get('attachment')
            attachment_id = request.env['ir.attachment'].sudo().create({
                'name': post.get('attachment').filename,
                'res_name': post.get('attachment').filename,
                'type': 'binary',
                'res_model': contract._name,
                'res_id': project_id,
                'datas': base64.b64encode(file.read()),
            })
            print("--------------------", attachment_id)
            contract.update({
                'attachment': [(4, attachment_id.id)]
            })
        return request.render("emp_contracts.emp_contracts_thanks", {})
