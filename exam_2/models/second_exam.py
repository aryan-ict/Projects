"""Model for Second Exam."""
from odoo import models, fields, api


class SecondExam(models.Model):
    _name = 'second.exam'
    _description = 'Exam 2'

    name = fields.Char(string="Name")
