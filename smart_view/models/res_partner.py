"""This model is to Inherit fields in Res Partner Model"""
from odoo import models, fields, api
import datetime


class ResPartner(models.Model):
    """This class is for inherited fields"""
    _inherit = 'res.partner'

    customer_ref = fields.Char(string="Customer Reference")
    birth_date = fields.Date(string="Birth Date")
    age = fields.Integer(string="Age", compute="_compute_calculate_age")
    customer_rank = fields.Integer(string="Customer Rank")

    def name_get(self):
        """Function for getting the list of full names."""
        res = []
        for rec in self:
            if self._context.get('cus_country'):
                print("rec--------", rec)
                if rec.customer_ref:
                    res.append((rec.id, '%s %s' % (rec.name, rec.customer_ref)))
                else:
                    res.append((rec.id, '%s %s' % (rec.name, rec.parent_id.name)))
            elif rec.parent_id.name:
                res.append((rec.id, '%s %s' % (rec.name, rec.parent_id.name)))
            else:
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

    @api.onchange('customer_rank')
    def onchange_customer_rank(self):
        """Function to get 'Best Customer' tag when customer rank > 5"""
        for rec in self:
            ids = [19]
            if rec.customer_rank > 5:
                self.write({'category_id': [(6, 0, ids)]})
            else:
                self.write({'category_id': [(6, 0, [1, 2, 3, 4])]})
