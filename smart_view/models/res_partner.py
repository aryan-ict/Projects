"""This model is to Inherit fields in Res Partner Model"""
from odoo import models, fields, api
import datetime


class ResPartner(models.Model):
    """This class is for inherited fields"""
    _inherit = 'res.partner'

    customer_ref = fields.Char(string="Customer Reference")
    birth_date = fields.Date(string="Birth Date")
    age = fields.Integer(compute="_compute_calculate_age", string="Age")

    def name_get(self):
        """Function for getting the list of full names."""
        res = []
        if self._context.get('cus_country'):
            for rec in self:
                print("rec--------", rec)
                if rec.customer_ref:
                    res.append((rec.id, '%s %s' % (rec.name, rec.customer_ref)))
                else:
                    res.append((rec.id, '%s' % rec.name))
        else:
            for rec in self:
                res.append((rec.id, '%s' % rec.name))
        return res


@api.model
def _name_search(self, name, args=None, operator='ilike', limit=100):
    """Function for Name Search Method."""
    args = args or []
    domain = []
    if name:
        domain = ['|', '|', ('name', operator, name), ('phone', operator, name), ('email', operator, name)]
    return self._search(domain + args, limit=limit)


@api.depends('birth_date')
def _compute_calculate_age(self):
    """Function to calculate Age form Birth Date"""
    today_date = datetime.date.today()
    for rec in self:
        if rec.birth_date:
            rec.age = today_date.year - rec.birth_date.year - (
                    (today_date.month, today_date.day) < (rec.birth_date.month, rec.birth_date.day))
        else:
            rec.age = 0
        # rec.age = int((datetime.date.today() - rec.birth_date).days / 365)
