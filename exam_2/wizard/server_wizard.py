"""This model is for wizard."""
from odoo import models, fields, api


class ServerWizard(models.TransientModel):
    """This class contains fields for wizard"""
    _name = "server.wizard"

    sale_order_ids = fields.One2many('server.wizard.otm', 'product_qty', string="Sale Order")

    def create_so(self):
        """Function to get order lines on the
        click of the button in wizard."""
        for rec in self:
            new_lines = []
            for res in rec.sale_order_ids:
                new_lines.append((0, 0, {
                    'product_id': res.product_id.id,
                    'product_uom': res.price_unit,
                    'product_uom_qty': res.product_qty
                }))
            print("-----------------------", self._context)
            vals = self.env['sale.order'].create({'order_line': new_lines})
            print("-------------------------", new_lines)
            print("-------------------------", vals)
            print("-------------------------", )
            return vals


class ServerWizardOtm(models.TransientModel):
    """This class is for One2many Field."""
    _name = 'server.wizard.otm'
    _description = 'Server Wizard One2many'

    product_id = fields.Many2one('product.product', string="Product")
    product_qty = fields.Integer(string="Product Quantity")
    price_unit = fields.Float(string="Unit Price", related="product_id.list_price")
