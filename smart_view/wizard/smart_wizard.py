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

    @api.model
    def default_get(self, fields):
        """Function for Default Get Method"""
        res = super(SmartWizard, self).default_get(fields)
        rec = self.env['sale.order'].browse(self.env.context.get('active_id'))
        print("fields----\n", fields)
        print("res----\n", res)
        print("rec----\n", rec)

        res.update({
            'partner_id': rec.partner_id.id,
            'email': rec.partner_id.email,
            'sales_person': rec.user_id.id,
            'sales_contact': rec.user_id.phone,
            'payment_term_id': rec.payment_term_id.id
        })
        return res
