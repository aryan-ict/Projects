from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import *


class OrganizationAdvertise(models.Model):
    _name = "orphans.advertise"
    _description = "organization advertise"

    organization_id = fields.Many2one('orphans.organization', string="Organization Home")
    avl_seats = fields.Integer(string="Available Seats")
    exp_dates = fields.Date(string="Expired Dates")
    facilities = fields.Html(string="Facilities")
    s1 = fields.Char(string="Address",related="organization_id.street1")
    s2 = fields.Char(related="organization_id.street2")
    city = fields.Char(related="organization_id.city")
    state = fields.Many2one(related="organization_id.state_id")
    zip = fields.Char(related="organization_id.zip")
    country = fields.Many2one(related="organization_id.country_id")
    image = fields.Binary()

    def s_button(self):
        print("works")

    # @api.depends('')