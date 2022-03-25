

from odoo import models, fields, api


class orphans_organization(models.Model):

    _name = 'orphans.organization'
    _description = 'orphans_organization'

    name = fields.Char(required=True)
    o_image = fields.Binary()
    s1 = fields.Char(string="Address")
    s2 = fields.Char()
    city = fields.Char()
    state = fields.Char()
    zip = fields.Char()
    country = fields.Char()
    ngo_id = fields.Many2one('res.partner', string="NGO", domain=[('ngo_check', '=', True)])

    # total_member_orphan = fields.Integer(string="Total Orphan Members")
    # available_fund = fields.Integer(string="Available Funds")
    foundation_years = fields.Selection(selection="foundation_y", string="Foundation Year")
    total_capacity = fields.Integer(string="Total Capacity")
    orphan_member = fields.Char(string='Orphan Member')

    def foundation_y(self):
        x = [(str(i), i) for i in range(1990, 2022)]
        return x
        # return tuple(enumerate(x))

    def s_button(self):
        pass

    def s2_button(self):
        pass

    def name_get(self):
        """Function To Concatenate Name, NGO, State fields."""
        res = []
        for rec in self:
            if rec.state:
                res.append((rec.id, '%s (%s, %s)' % (rec.name, rec.ngo_id.name, rec.state)))
            else:
                res.append((rec.id, '%s (%s)' % (rec.name, rec.nago_id.name)))
        return res



