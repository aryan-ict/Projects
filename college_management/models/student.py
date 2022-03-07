# -*- coding: utf-8 -*-

from odoo import models, fields, api

'''
Creating a class with name college_management.
Using models.Model giving the type of model.
Assigning name for the model which is college_management.college_management.
Description is about describing the model is about College Management.
'''


class student_form(models.Model):
    _name = "student.form"
    # _inherit = ["sale.order"]
    _description = "Student Form"

    phone_no = fields.Integer(string="Phone")
    email_id = fields.Char(string="Email")