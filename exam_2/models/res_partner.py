"""This model is for Res Partner."""
from odoo import models, fields, api
import datetime


class ResPartner(models.Model):
    """This class inherits res.partner"""
    _inherit = 'res.partner'

    birth_date = fields.Date(string="Birth Date")
    age = fields.Integer(string="Age", compute="_compute_age")

    @api.depends('birth_date')
    def _compute_age(self):
        """Function To calculate When Birthdate is selected."""
        for rec in self:
            if rec.birth_date:
                rec.age = (datetime.date.today() - rec.birth_date).days / 365
            else:
                rec.age = 0
