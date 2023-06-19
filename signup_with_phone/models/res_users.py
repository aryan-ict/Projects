# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class ResUsers(models.Model):
    _inherit = "res.users"

    login_email = fields.Char(string="Email")
