"""This model is for Inheritance in product.template model"""

from odoo import models, fields


class ProductTemplateInherit(models.Model):
    """This class is for fields which will be inherited"""
    _inherit = "product.template"

    is_rental = fields.Boolean(string="Is Rental")
    rental_type_id = fields.Many2one('rental.type', string="Rental Type")
