"""This model is for Invoicing."""
from odoo import models, fields, api


class AccountMoveLine(models.Model):
    """This class is for fields inherited in Invoice Lines."""
    _inherit = 'account.move.line'
    _description = 'Invoice Lines'

    product_length = fields.Float(string="Length", related="product_id.product_length")
    product_total_length = fields.Float(string="Total Length", compute='_compute_total_length', store=True)

    @api.depends('product_length', 'quantity')
    def _compute_total_length(self):
        """Function To compute Total Length."""
        for rec in self:
            if rec.product_length and rec.quantity:  # here it will check if fields are empty or not.
                total_length = rec.product_length * rec.quantity
                print("`````````````````````````````total", total_length)
                self.product_total_length = total_length
