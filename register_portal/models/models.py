# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime


class register_portal(models.Model):
    _name = 'register_portal.register_portal'
    _description = 'register_portal.register_portal'
    _rec_name = 'name'

    name = fields.Char()
    value = fields.Integer()
    value2 = fields.Float(string="VALUE2", compute="_value_pc", store=True)
    description = fields.Text()
    age = fields.Integer()
    dob = fields.Date(default=datetime.today())
    male = fields.Boolean()
    female = fields.Boolean()
    file_upload = fields.Binary()
    country = fields.Many2one('res.country', string='country')
    # city = fields.One2many('res.users', string='city')
    mobile = fields.Integer(string="Mobile")





    @api.depends('value')
    def _value_pc(self):
        for record in self:
            record.value2 = float(record.value) / 100
