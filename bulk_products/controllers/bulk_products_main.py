from odoo import http, _
from odoo.http import request


class Website(http.Controller):
    @http.route('/bulk_products', type='http', auth='user', website=True)
    def bulk_product_form(self):
        bulk_list = request.env['bulk.products'].search([])
        return request.render('bulk_products.bulk_products_list', {
            'bulk_list': bulk_list
        })
