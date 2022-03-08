# -*- coding: utf-8 -*-

from odoo import models, fields, api


class database(models.Model):
    _name = 'database.database'
    _description = 'database.database'

    name = fields.Char()
    value = fields.Integer()
    value2 = fields.Float(compute="_value_pc", store=True)
    description = fields.Text()
    my_selection_field = fields.Selection([('option1', 'Label 1'), ('option2', 'Label 2')], string='My Selection Field')
    student_degree = fields.Selection([('option0', 'None'), ('option1', 'CE'),('option', 'ICT')], default='option0', string='Student Degree')
    @api.depends('value')
    def _value_pc(self):
        for record in self:
            record.value2 = float(record.value) / 100
