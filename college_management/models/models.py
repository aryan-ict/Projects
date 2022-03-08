"""This module is For Practice"""
from odoo import models, fields


class CollegeManagement(models.Model):
    """This class is for fields and ORM methods"""
    _name = "college.management"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Model for College Management"


    name = fields.Char(string='Name')
    last_name = fields.Char(string='Last Name')
    mobile_no = fields.Char(string='Mobile Number')
    description = fields.Text()
    select_type = fields.Selection([('option1', 'Graduation'),
                                    ('option2', 'Post Graduation')],
                                   string="Degree Type",
                                   tracking=True)
    dob = fields.Date(string='Date Of Birth')
    status = fields.Selection(
        [('draft', 'Draft'), ('process', 'In Process'),
         ('confirm', 'Confirm'), ('cancelled', 'Cancelled')],
        default='draft', string='Status', tracking=True)
    full_name = fields.Many2one('college.management', string='Full Name')

    def sample_button_d(self):
        """Function for sample button
        unlinks record"""
        self.unlink()

    def create_button(self):
        """Function for create button
        creates new values
        :return: None"""
        vals1 = {'name': 'Kavish',
                 'mobile_no': '03'}
        self.create(vals1)

    def write_button(self):
        """Function for write button
        writes new values
        :return: None"""
        vals = {'name': 'Aryan',
                'mobile_no': '02',
                'description': 'Odoo Trainee',
                'select_type': 'option1'
                }
        self.write(vals)

    def unlink_button(self):
        """Function for unlink button
        unlinks the selected record
        :return: None"""
        self.unlink()

    def name_get(self):
        """Function for getting the list of full names."""
        res = []
        for rec in self:
            print("rec--------", rec)
            res.append((rec.id, '%s %s' %(rec.name, rec.last_name)))
        return res
