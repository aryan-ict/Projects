# -*- coding: utf-8 -*-

from odoo import models, fields, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'
    sale_test = fields.Char(string='Customer Reference',  related='partner_id.customer_reference',)


