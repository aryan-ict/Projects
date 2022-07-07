from odoo import models, fields, api, _


class NewOrderLine(models.Model):
    _name = "new.order.line"
    _description = "New Order Line"

    product_id = fields.Many2one('product.product', string="Product")
    name = fields.Text(string="Description")
    product_uom_qty = fields.Float(string="Quantity")
    price_unit = fields.Float(string="Unit Price")
    sale_order_id = fields.Many2one('sale.order', ondelete='cascade')
    price_subtotal = fields.Float(string="Subtotal")
