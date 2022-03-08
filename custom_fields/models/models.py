# -*- coding: utf-8 -*-

from odoo import models, fields, api


class custom_fields(models.Model):
    _name = 'custom_fields.custom_fields'
    _description = 'custom_fields.custom_fields'

    name = fields.Char()
    value = fields.Integer()
    description = fields.Text()

