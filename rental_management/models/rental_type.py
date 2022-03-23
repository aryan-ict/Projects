"""This model is for sub menu in Rental Management."""

from odoo import models, fields, api


class RentalType(models.Model):
    """This class is for fields"""
    _name = "rental.type"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Model for sub menu Rental Type"
    _rec_name = "type_name"

    type_name = fields.Char(string="Name", tracking=True, required=False)
    code = fields.Char(string="Code")
    description = fields.Text(string="Description")
