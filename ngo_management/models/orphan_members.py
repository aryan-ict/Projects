from odoo import fields, models


class orphans_member(models.Model):
    _name = 'orphans.member'
    _description = "Orphans request can accept and add by managers and users"

    name = fields.Char(string="Name", required=True)
    dob = fields.Date(string="DOB", required=True, help="Date of Birth")
    guardian_name = fields.Char(string="Guardian Name")
    organization_name = fields.Char(string="Orphan Organization", required=True)
    organizationid = fields.Integer()
    ngo_name=fields.Char()
    age = fields.Char(string="Age", required=True)
    street1 = fields.Char(string='Address')
    street2 = fields.Char()
    city = fields.Char()
    state = fields.Char()
    zip = fields.Char()
    country = fields.Char()
    address = fields.Text(string='Address', compute='addr_field')

    def addr_field(self):
        self.address = ",\n".join([str(self.street1),
                                   str(self.street2),
                                   str(self.city),
                                   str(self.state),
                                   str(self.country),
                                   str(self.zip)])
