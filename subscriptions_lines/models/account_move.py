"""This model is for Invoicing."""
import random
import string
from odoo import models, fields, api
from odoo.exceptions import ValidationError


class AccountMoveLine(models.Model):
    """This class is for fields inherited in Invoice Lines."""
    _inherit = 'account.move'
    _description = 'Invoice'

    token_no = fields.Char(string="Token No", readonly=True)

    def generate_bill(self):
        """This function creates Bills based on
         Vendors selected in invoice_line_ids."""
        vendor_ids = self.invoice_line_ids.mapped("vendor_id.id")
        if self.state == 'posted':
            for res in vendor_ids:
                new_lines = []
                for rec in self.invoice_line_ids.filtered(lambda x: x.vendor_id.id == res):
                    new_lines.append((0, 0, {
                        'product_id': rec.product_id,
                        'price_unit': rec.vendor_price
                    }))
                self.create({
                    'move_type': 'in_invoice',
                    'partner_id': res,
                    'invoice_line_ids': new_lines
                })
        else:
            raise ValidationError("The State of invoice must be Posted.")

    def generate_number(self):
        """Function to generate random number
        on the click of button."""
        num1 = random.choice(string.digits)
        num2 = random.choice(string.ascii_letters)
        num3 = random.choice(string.ascii_letters)
        self.token_no = num1 + num2 + num3 + "-M"
