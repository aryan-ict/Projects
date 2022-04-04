from odoo import models, fields, api


class TimesheetWizard(models.TransientModel):
    _name = 'timesheet.wizard'

    employee_ids = fields.Char(string="Employee")
    start_date = fields.Date(string="Start Date")
    end_date = fields.Date(string="End Date")