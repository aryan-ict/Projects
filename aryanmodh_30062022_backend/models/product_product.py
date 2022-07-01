from odoo import models, fields, api, _


class ProductProduct(models.Model):
    _inherit = 'product.product'

    product_length = fields.Float(string="Length")
