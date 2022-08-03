from odoo import models, fields, api, _


class StudentWebsitePortal(models.Model):
    _name = "student.website.portal"
    _description = "Student Website Portal"

    name = fields.Char()
    street = fields.Char()
    street2 = fields.Char()
    zip = fields.Char()
    city = fields.Char()
    state = fields.Many2one('res.country.state', 'Fed. State',
                            domain="[('country_id', '=?', country)]")
    country = fields.Many2one('res.country')
    phone = fields.Char('Phone')
    email = fields.Char('Email')
    birth_date = fields.Date('Birth Date')
    allocated_id = fields.Many2one('res.users', string="Allocated Teacher")


