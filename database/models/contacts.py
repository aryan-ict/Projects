# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime


class customerView(models.Model):
    _inherit = 'res.partner'
    birth_date = fields.Date(string="Birth Date", required=True)
    customer_reference = fields.Char(string="Customer Reference")
    street3 = fields.Char(string="Street 3")
    description = fields.Char(string="Description")
    age = fields.Char(string="Age")


