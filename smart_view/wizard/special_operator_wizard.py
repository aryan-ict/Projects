"""This model is for Special Operators Wizard."""
from odoo import models, fields, api


class SpecialOperatorWizard(models.TransientModel):
    """This class is for fields and function."""
    _name = "special.operator.wizard"

    product_ids = fields.Many2many('sale.order.line', string="Products")

    def create_order_line(self):
        """Function to get order lines on the
        click of the button in wizard."""
        res = self.env['sale.order'].browse(self.env.context.get('active_id'))
        for rec in self.product_ids:
            res.create({'order_line': (4, rec.id)})
