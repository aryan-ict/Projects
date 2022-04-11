from odoo import models, fields, api
import xlwt
from xlwt import easyxf
import base64
from io import BytesIO
from dateutil.relativedelta import relativedelta


class TimesheetWizard(models.TransientModel):
    _name = 'timesheet.wizard'

    employee_ids = fields.Many2many('hr.employee', string="Employee")
    start_date = fields.Date(string="Start Date")
    end_date = fields.Date(string="End Date")
    excel_file = fields.Binary()

    _sql_constraints = [
        ('check', 'CHECK((start_date <= end_date))', "End Date  must be Greater than Start Date")
    ]

    def timesheet_report_button(self):
        file_name = 'Timesheet'
        workbook = xlwt.Workbook(encoding="UTF-8")
        worksheet = workbook.add_sheet("Timesheet")
        header_style = easyxf('font:height 500; align: horiz center; font:bold True; borders: top_color black, '
                              'bottom_color black, right_color black, left_color black, left thin, right thin, '
                              'top thin, bottom thin;')
        format_1 = xlwt.easyxf('font:bold True; align: horiz center; borders: top_color black, bottom_color black, '
                               'right_color black, left_color black, left thin, right thin, top thin, bottom thin;')
        format_2 = xlwt.easyxf('align: horiz center;')
        worksheet.write_merge(6, 7, 3, 7, "Timesheet", header_style)
        worksheet.col(3).width = int(20 * 260)
        worksheet.col(4).width = int(25 * 260)
        worksheet.col(5).width = int(30 * 260)
        worksheet.col(6).width = int(20 * 260)
        worksheet.col(7).width = int(15 * 260)
        worksheet.write(8, 3, 'Employee Name', format_1)
        worksheet.write(8, 4, 'Project', format_1)
        worksheet.write(8, 5, 'Task', format_1)
        worksheet.write(8, 6, 'Description', format_1)
        worksheet.write(8, 7, 'Hours', format_1)
        row = 8
        for rec in self.employee_ids:
            row += 1
            col = 3
            worksheet.write(row, col, rec.name)
            new_row = row
            for project in self.env['account.analytic.line'].search(
                    [('employee_id', '=', rec.id), ('date', '>=', self.start_date),
                     ('date', '<=', self.end_date)]):
                col = 4
                worksheet.write(new_row, col, project.project_id.name)
                new_row += 1
            new_row = row
            for task in self.env['account.analytic.line'].search([('employee_id', '=', rec.id)]):
                col = 5
                worksheet.write(new_row, col, task.task_id.name)
                new_row += 1
            new_row = row
            for description in self.env['account.analytic.line'].search([('employee_id', '=', rec.id)]):
                col = 6
                worksheet.write(new_row, col, description.name)
                new_row += 1
            new_row = row
            tot_hours = 0
            for hours in self.env['account.analytic.line'].search([('employee_id', '=', rec.id)]):
                col = 7
                worksheet.write(new_row, col, hours.unit_amount, format_2)
                tot_hours += hours.unit_amount
                new_row += 1
            row = new_row
            worksheet.write(row, 7, tot_hours)
            row += 1
            # print("---------------------------", row)
            # formula = xlwt.Formula('SUM(H9:H17)')
            # worksheet.write(row, 7, formula)
            # print("-------------------", formula)

        fp = BytesIO()
        workbook.save(fp)
        fp.seek(0)
        excel_file = base64.encodebytes(fp.getvalue())
        fp.close()
        self.write({
            'excel_file': excel_file
        })
        url = ('web/content/?model=timesheet.wizard&download=true&field=excel_file&id=%s&file_name=%s' % (
            self.id, file_name))
        if self.excel_file:
            return {
                'type': 'ir.actions.act_url',
                'url': url,
                'target': 'new'
            }
