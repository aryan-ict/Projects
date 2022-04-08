"""This model is for wizard."""
from odoo import models, fields, api


class ServerWizard(models.TransientModel):
    """This class contains fields for wizard"""
    _name = "server.wizard"

    sale_order_ids = fields.One2many('server.wizard.otm', 'test_id', string="Sale Order")

    def create_so(self):
        """Function to get order lines on the
        click of the button in wizard."""
        new_lines = []
        for res in self.sale_order_ids:
            new_lines.append((0, 0, {
                'product_id': res.product_id.id,
                'product_uom_qty': res.product_qty
            }))
        print("-----------------------", self._context)
        for rec in self._context.get('active_ids'):
            vals = self.env['sale.order'].create({'partner_id': rec, 'order_line': new_lines})
            print("-------------------------", vals)
        print("-------------------------", new_lines)


class ServerWizardOtm(models.TransientModel):
    """This class is for One2many Field."""
    _name = 'server.wizard.otm'
    _description = 'Server Wizard One2many'

    product_id = fields.Many2one('product.product', string="Product")
    product_qty = fields.Float(string="Product Quantity")
    price_unit = fields.Float(string="Unit Price", related="product_id.list_price")
    test_id = fields.Many2one('server.wizard')
