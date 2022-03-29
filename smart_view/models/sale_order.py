"""This model is to Inherit fields in Sale Order Model"""

from odoo import models, fields, api
from odoo.exceptions import UserError


class SaleOrder(models.Model):
    """This class is for inherited fields"""
    _inherit = 'sale.order'

    mobile = fields.Char(string="Mobile")
    email = fields.Char(string="Email")
    customer_ref = fields.Char(string="Customer Reference", related='partner_id.customer_ref')
    customer_rank = fields.Integer(string="Customer Rank", related='partner_id.customer_rank''')

    @api.onchange('partner_id')
    def onchange_partner_id(self):
        """Function to relate the fields."""
        for rec in self:
            if rec.partner_id:
                rec.mobile = rec.partner_id.phone
                rec.email = rec.partner_id.email

    # @api.constrains('payment_term_id')
    # def check_terms(self):
    #     """Function to """
    #     for rec in self:
    #         if rec.payment_term_id not in rec.partner_id.property_payment_term_id:
    #             raise UserError("Use same Payment Terms")

    def action_confirm(self):
        """Function to override the Confirm Button in Sale Order."""
        for rec in self:
            if len(rec.order_line) > 3:
                raise UserError("Can not add more than 3 orders at the moment.")
            else:
                return super(SaleOrder, self).action_confirm()

    @api.onchange('customer_rank')
    def onchange_customer_rank(self):
        """Function To get 'Best Customer' when customer rank > 5"""
        for rec in self:
            if rec.customer_rank > 5:
                self.write({'tag_ids': [(6, 0, [9])]})
            else:
                self.write({'tag_ids': [(6, 0, [1, 2, 3, 4, 10])]})
