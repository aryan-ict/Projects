"""This model is for Special Operators Wizard."""
from odoo import models, fields, api


class SpecialOperatorWizard(models.TransientModel):
    """This class is for fields and function."""
    _name = "special.operator.wizard"

    product_ids = fields.Many2many('product.product', string="Products")

    def create_order_line(self):
        """Function to get order lines on the
        click of the button in wizard."""
        res = self.env[self._context.get('active_model', [])].browse(self.env.context.get('active_ids', []))
        for rec in self.product_ids:
            res.write({'order_line': [(0, 0, {'product_id': rec.id})]})
