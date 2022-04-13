"""This model is for subscriptions lines"""
from odoo import models, fields, api


class SubscriptionsLines(models.Model):

    _name = "subscriptions.lines"

    name = fields.Char(string="Name")
    phone = fields.Char(string="Phone")
