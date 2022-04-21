
from odoo import models , fields , api

class OrphansDonation(models.Model):

    _name = 'orphans.organization.donation'
    _description = 'orphans_donation'

    name = fields.Char(required=True , string="Doner Name")
    organization_id = fields.Many2one('orphans.organization', string="Orphans Home")
    ngo_id = fields.Many2one(string="Ngo",
                             related="organization_id.ngo_id")
    amount = fields.Integer(string="Amount", required=True)
    phone = fields.Char(string="Phone No")
    email = fields.Char(string="Email")

    s1 = fields.Char(string="Address")
    s2 = fields.Char()
    city = fields.Char()
    state_id = fields.Many2one('res.country.state')
    zip = fields.Char()
    country_id = fields.Many2one('res.country')

    @api.onchange('state_id')
    def onchange_country(self):
        print("\n -------------------------------------------",self.state_id.id)
        self.country_id = self.state_id.country_id

    def s_button(self):
        pass

    # @api.model_create_multi
    # def create(self, vals):
    #     print("\n\nFUnction Called\n\n")
    #     res_id = super(OrphansDonation, self).create(vals)
    #     org = self.env["orphans.organization"]
    #     for rec in vals:
    #         print("loop run")
    #         print(rec['amount'] , vals)
    #         if rec['amount']:
    #             print('if True\n\n')
    #             amount = rec['amount']
    #             print(amount)
    #             org_id = org.browse(rec['organization_id'])
    #             print("\n\n\n ",org_id.amount)
    #             org_id.amount += amount
    #             print(org_id.amount, amount, "\n")
    #     return res_id
