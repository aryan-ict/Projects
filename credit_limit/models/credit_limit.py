from odoo import models, fields, api, _


class CreditLimit(models.Model):
    _name = "credit.limit"
    _description = "Credit Limit & Block Limit"

    name = fields.Char('name')
