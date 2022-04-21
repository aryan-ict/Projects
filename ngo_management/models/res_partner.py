"""
inherited view
"""

from odoo import models, fields, api


class ResPartner(models.Model):
    _inherit = 'res.partner'

    _description = 'Res Partner'

    ngo_check = fields.Boolean(string="NGO")
    orphan_members = fields.Integer(compute='total_orphan_members')

    @api.onchange('company_type')
    def onchange_company_type_ngo(self):
        for rec in self:
            if rec.company_type == 'person':
                rec.ngo_check = False



    def total_orphan_members(self):

        """
        counting courses 'not yet complete'
        """
        for rec in self:
            res = self.env['orphans.member'].search_count([("ngo_name", "=", rec.name)])
            rec.orphan_members = res


    def total_available_funds(self):
        pass

