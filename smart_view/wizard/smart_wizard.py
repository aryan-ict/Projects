"""This model is for wizard."""
from odoo import models, fields, api


class SmartWizard(models.TransientModel):
    """This class contains fields for wizard"""
    _name = "smart.wizard"
    _description = "Model for Wizard"

    customer_id = fields.Many2one('res.partner', string="Customer")
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
            'customer_id': rec.partner_id.id,
            'email': rec.partner_id.email,
            'sales_person': rec.user_id.id,
            'sales_contact': rec.user_id.phone,
            'payment_term_id': rec.payment_term_id.id
        })
        return res

    def create_wizard2(self):
        context = self._context
        rental_type = self.env[context["active_model"]].browse(context["active_id"])
        rental_type.create({
            'partner_id': self.customer_id.id,
            'email': self.email,
            'user_id': self.sales_person,
            'mobile': self.sales_contact,
            'payment_term_id': self.payment_term_id
        })
        # print("========================>", res)
