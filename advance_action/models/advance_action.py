"""This model is for Advance Action."""

from odoo import models, fields, api


class AdvanceAction(models.Model):
    """This class is for simple fields."""
    _name = 'advance.action'
    _description = 'Advance Action Model'

    name = fields.Char(string="Name")
    last_name = fields.Char(string="Last Name")

    def server_action(self):
        vals = {'name': "Parth",
                'last_name': '1123456789',
                }
        self.create(vals)
