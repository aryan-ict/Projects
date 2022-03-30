"""This model is for Advance Action."""

from odoo import models, fields, api


class SaleOrder(models.Model):
    """This class is for Scheduler Action Function."""
    _inherit = 'sale.order'

    def change_state(self):
        self.search([]).write({'state': 'sent'})
        # print("----------------------Hello World")
        # lst = []
        # for rec in self.search([]):
        #     lst.append(rec.id)
        # print("--------------------", lst)
        # res = self.browse(lst)
        # print("----------------------", res)
        # if res:
        #     res.state = 'draft'
