from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import *


class OrphansRequest(models.Model):
    _name = "orphans.request"
    _description = "orphans request"

    name = fields.Char(required=True)
    dob = fields.Date(string="Date Of Birth", required=True)
    guardian_name = fields.Char(string="Guardian Name")
    age = fields.Char(string="Age", compute="cal_dob", store=True)
    s1 = fields.Char(string="Address")
    s2 = fields.Char()
    city = fields.Char()
    state_id = fields.Many2one('res.country.state')
    zip = fields.Char()
    country_id = fields.Many2one('res.country')

    organization_id = fields.Many2one(comodel_name='orphans.organization', string="Organization Name")
    ngo_id = fields.Many2one(string="Ngo",
                             related="organization_id.ngo_id")

    state = fields.Selection(
        selection=[('draft', 'Draft'), ('send', 'Send'), ('confirm', 'Confirm'), ('cancel', 'Cancel')], default='draft')

    @api.onchange('state_id')
    def onchange_country(self):
        self.country_id = self.state_id.country_id

    @api.model
    def default_get(self, fields):
        defaults = super(OrphansRequest, self).default_get(fields)
        defaults['organization_id'] = self.env["orphans.advertise"].browse(self.env.context.get("active_id"))
        return defaults

    @api.depends("dob")
    def cal_dob(self):
        if self.dob is not False:
            for i in self:
                today = date.today()
                i.age = today.year - i.dob.year - ((today.month - today.day) < (i.dob.month - i.dob.day))

    def val_age(self):
        if int(self.age) > 18:
            raise ValidationError("Age Must Be Below 18 !")
        else:
            self.write({'state': 'send'})

    def Approve_button(self):

        for record in self:
            req_details = {
                'name': record.name,
                'guardian_name': record.guardian_name,
                'organization_name': record.organization_id.name,
                'organizationid': record.organization_id.id,
                'ngo_name': record.ngo_id.name,
                'age': record.age,
                'dob': str(record.dob),
                'street1': record.s1,
                'street2': record.s2,
                'city': record.city,
                'state': record.state_id,
                'zip': record.zip,
                'country': record.country_id
            }
        for i, j in req_details.items():
            print(i, '\t\t:', j)

        member_req = self.env['orphans.member']
        member_req.create(req_details)

        self.write({'state': 'confirm'})

    def Cancel_button(self):
        self.write({'state': 'cancel'})
