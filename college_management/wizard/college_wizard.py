"""This model is for College Management Wizard"""
from odoo import models, fields, api


class College_Management(models.TransientModel):
    """This class is for fields in wizard"""
    _name = 'college.wizard'
    _description = 'Wizard1'

    name = fields.Many2one("res.partner", string="Name")
    mobile = fields.Integer(string="Mobile Number")
    address = fields.Text(string="Address")
    country = fields.Many2one('res.country', string='Country')
    course = fields.Selection([('O1', "Diploma"), ('O2', "Graduation"), ('O3', 'Post Graduation')],
                              string="Course Type")
    upload = fields.Binary(string="File Upload")
    interests = fields.Many2many('res.partner.category', string="Your Interests")
    signature = fields.Binary(string="Signature")
    image = fields.Binary(string="Upload Image")

    def submit_button(self):
        """Function for Submit button"""
        print("Submit Button")


