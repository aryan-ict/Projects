from odoo import models, fields, api, _


class SaleOrder(models.Model):
    _inherit = "sale.order"
    _description = "Sale Order"

    product_id = fields.Many2one('product.product', string="Product")
    qty = fields.Float(string="Quantity")

    @api.onchange('product_id', 'qty')
    def _onchange_bulk_product(self):
        """Function to add lines onchange of QTY field and Product field."""
        print("--------------------------testing")
        new_lines = []
        if self.qty:
            print("````````````````````````````````new_lines", new_lines)
            if self.product_id not in self.order_line.product_id:  # here it will check for product repetition.
                new_lines.append((0, 0, {  # here it will append all the values of fields in a list.
                    'product_id': self.product_id.id,
                    'name': self.product_id.name,
                    'product_uom_qty': self.qty,
                    'product_length': self.product_id.product_length,
                    'price_unit': self.product_id.list_price,
                    'product_uom': self.product_id.uom_id.id
                }))
                self.order_line = new_lines  # assigning the list to order line.
            for rec in self.order_line:
                if self.product_id in rec.product_id:
                    self.write({'order_line': [(1, rec.id, {'product_uom_qty': self.qty})]
                                })
                print("--------------------------new_lines", new_lines)

    def _prepare_invoice_line(self, order_line):
        print("---------------------vals", order_line)
        res = super(SaleOrderLine, self)._prepare_invoice_line(order_line)
        res.update({
            'product_length': order_line.product_length,
            'product_total_length': order_line.product_total_length
        })
        return res

        # elif self.product_id in self.order_line.product_id:
        #     for rec in self.order_line:
        #         print("---------------------------rec", rec)
        #         if self.product_id in rec.product_id:
        #             self.update((1, rec.id, {'order_line': {
        #                 'product_uom_qty': self.qty
        #             }}))
    #     for res in self.product_id:
    #         if rec.order_line.product_id.id == res.product_id.id:
    #             self.order_line.product_uom_qty = rec.qty
    # if rec.product_id in rec.order_line.product_id:
    #     self.write({
    #         'order_line': {'product_uom_qty': rec.qty}
    #     })
