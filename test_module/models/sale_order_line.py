from odoo import models, fields, api


class SaleOrderLine(models.Model):
    """This class is for fields inherited in Invoice Lines."""
    _inherit = 'sale.order.line'
    _description = 'Order Line'

    product_length = fields.Float(string="Length")
    product_total_length = fields.Float(string="Total Length", compute='_compute_total_length', store=True)

    @api.depends('product_length', 'product_uom_qty')
    def _compute_total_length(self):
        """Function To compute Total Length."""
        for rec in self:
            if rec.product_length and rec.product_uom_qty:  # here it will check if fields are empty or not.
                total_length = rec.product_length * rec.product_uom_qty
                print("`````````````````````````````total", total_length)
                self.product_total_length = total_length

    @api.depends('product_uom_qty', 'product_length', 'price_unit')
    def _compute_amount(self):
        """Function To compute Subtotal field of Sale Order Line"""
        res = super(SaleOrderLine, self)._compute_amount()  # here used base function for subtotal compute
        for line in self:
            if line.product_uom_qty and line.product_length and line.price_unit:
                line.price_subtotal = line.product_uom_qty * line.product_length * line.price_unit
        return res
