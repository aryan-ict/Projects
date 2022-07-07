from odoo import models, fields, api, _


class SaleOrder(models.Model):
    _inherit = "sale.order"
    _description = "Sale Order"

    new_order_line_ids = fields.One2many('new.order.line', 'sale_order_id')

    def write(self, vals):
        res = super(SaleOrder, self).write(vals)
        print("=================vals", vals)
        print("-----------------vals details", vals.get('order_line'))
        print("=================self", self.order_line.product_id)
        print("=================self", self.new_order_line_ids)
        new_line = []
        for rec in self.order_line:
            if rec.product_id not in self.new_order_line_ids.product_id:
                print("-----------------rec", rec.product_id)
                new_line.append((0, 0, {
                    'product_id': rec.product_id.id,
                    'name': rec.name,
                    'product_uom_qty': rec.product_uom_qty,
                    'price_unit': rec.price_unit,
                    'price_subtotal': rec.price_subtotal
                }))
                self.update({
                    'new_order_line_ids': new_line
                })

        # self.write({'new_order_line_ids': [(2, line.id) for line in self.order_line]})
        print("```````````````new_line", new_line)
        return res
