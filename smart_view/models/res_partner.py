"""This model is to Inherit fields in Res Partner Model"""
from odoo import models, fields, api


class ResPartner(models.Model):
    """This class is for inherited fields"""
    _inherit = 'res.partner'

    customer_ref = fields.Char(string="Customer Reference")

    def name_get(self):
        """Function for getting the list of full names."""
        res = []
        for rec in self:
            print("rec--------", rec)
            res.append((rec.id, '%s %s' % (rec.name, rec.customer_ref)))
        return res

    @api.model
    def _name_search(self, name, args=None, operator='ilike', limit=100):
        args = args or []
        domain = []
        if name:
            domain = ['|', '|', ('name', operator, name), ('phone', operator, name), ('email', operator, name)]
        return self._search(domain + args, limit=limit)
