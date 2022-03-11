"""This model is for wizard."""
from odoo import models, fields, api


class SmartWizard(models.TransientModel):
    """This class contains fields for wizard"""
    _name = "smart.wizard"
    _description = "Model for Wizard"

    partner_id = fields.Many2one('res.partner', string="Customer")
    email = fields.Char(string="Email")
    sales_person = fields.Many2one('res.users', string="Salesperson")
    sales_contact = fields.Char(string="Sales Person Contact")
    payment_term_id = fields.Many2one('account.payment.term', string="Payment Terms")

    # @api.model
    # def default_get(self, fields):
    #     """Function for Default Get Method"""
    #     res = super(SmartWizard, self).default_get(fields)
    #     print("fields----\n", fields)
    #     print("res----\n", res)
    #     res['email'] = res.email
    #     return res
