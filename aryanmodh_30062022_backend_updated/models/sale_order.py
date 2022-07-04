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
                    self.write({'order_line': [(1, rec.id, {'product_uom_qty': self.qty})]  # Here it will keep link of existing records and will make changes in selected record
                                })
                print("--------------------------new_lines", new_lines)
