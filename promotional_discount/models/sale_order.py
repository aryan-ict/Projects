from odoo import models, fields, api, _


class SaleOrder(models.Model):
    _inherit = "sale.order"
    _description = "Sale order"

    def apply_promotional_discount(self):
        pro_discount = self.env['product.product'].search([('default_code', '=', 'DISC')])
        promo_disc = self.env['promotional.discount'].search(
            [('start_date', '<=', self.date_order), ('end_date', '>', self.date_order)])
        print("-----------------------------discount", pro_discount)
        new_line = []
        for rec in promo_disc:
            if rec.discount_type == 'fixed':
                new_line.append((0, 0, {
                    'product_id': pro_discount.id,
                    'price_unit': "-" + str(rec.fixed_discount)
                }))
                self.update({
                    'order_line': new_line,
                })
            elif rec.discount_type == 'percentage':
                price = self.order_line.price_unit - (self.order_line.price_unit * (rec.discount / 100.0))
                print("-----------------price", price)
                new_line.append((0, 0, {
                    'product_id': pro_discount.id,
                    'price_unit': rec.discount
                }))
                self.update({
                    'order_line': new_line,
                    'amount_total': price
                })
                print("=============================new_line", new_line)
        print("----------------------------", self.tax_totals_json)
