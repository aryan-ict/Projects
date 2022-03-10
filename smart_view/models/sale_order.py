"""This model is to Inherit fields in Sale Order Model"""

from odoo import models, fields, api
from odoo.exceptions import UserError


class SaleOrder(models.Model):
    """This class is for inherited fields"""
    _inherit = 'sale.order'

    mobile = fields.Char(string="Mobile")
    email = fields.Char(string="Email")

    @api.onchange('partner_id')
    def onchange_partner_id(self):
        """Function to relate the fields."""
        for rec in self:
            if rec.partner_id:
                rec.mobile = rec.partner_id.phone
                rec.email = rec.partner_id.email

    @api.constrains('payment_term_id')
    def check_terms(self):
        """Function to """
        for rec in self:
            if rec.payment_term_id not in rec.partner_id.property_payment_term_id:
                raise UserError("Use same values")
