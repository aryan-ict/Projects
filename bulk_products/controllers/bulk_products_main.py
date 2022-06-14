from odoo import http, _
from odoo.http import request


class Website(http.Controller):
    @http.route('/bulk_products', type='http', auth='user', website=True)
    def bulk_product_form(self):
        bulk_list = request.env['bulk.products'].search([])
        return request.render('bulk_products.bulk_products_list', {
            'bulk_list': bulk_list
        })

    @http.route(['/bulk_products/details/<model("bulk.products"):bulk>'], type='http', auth='public', website=True)
    def bulk_details(self, bulk):
        print("----------------------bulk", bulk)
        return request.render("bulk_products.bulk_details", {'details': bulk})

    @http.route(['/bulk_products/bulk_create_form', '/bulk_products/bulk_create_form/<model("bulk.products"):record>'],
                type='http', auth='user', website=True)
    def bulk_form(self, record=None, **kw):
        master_id = request.env['product.template'].search([])
        user_id = request.env['res.partner'].search([])
        product_id = request.env['product.product'].search([])
        print('\n\nbulk---------------', record, '\n\n')
        print('\n\nkw---------------', kw, '\n\n')
        if kw:
            bulk_obj = request.env['bulk.products'].sudo()
            data = {
                'name': kw.get('name', False),
                'master_id': kw.get('master_id', False),
                'user_id': kw.get('user_id', False),
                'email': kw.get('email', False),
                'bulk_product_ids': kw.get('bulk_product_ids.product_id', False)
            }
            if kw.get('bulk_id', False):
                bulk_obj.browse(int(kw.get('bulk_id'))).write(data)
            else:
                bulk_obj.create(data)
            return request.redirect('/bulk_products')
        return request.render(
            "bulk_products.bulk_form", {'bulk': record,
                                        'master': master_id,
                                        'user': user_id,
                                        'product': product_id
                                        })

    # @http.route('/bulk_create_form/thank_you', type='http', auth='user', website=True)
    # def bulk_submit(self, **kw):
    #     if kw:
    #         request.env['bulk.products'].sudo().create(kw)
    #     return request.render('bulk_products.bulk_thank_you', {})
