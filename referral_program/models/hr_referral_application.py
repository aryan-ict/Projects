from odoo import models, fields, api


class HrReferralApplication(models.Model):
    _name = "hr.referral.application"
    _description = "Model for Referral Program"

    name = fields.Char(string="Name")
    email = fields.Char(string="Email")
    referral_id = fields.Many2one('hr.employee', string="Referral Name")
    degree_id = fields.Many2one('hr.recruitment.degree', string="Degree")
    department_id = fields.Many2one('hr.job', string="Department")
    expected_salary = fields.Float(string="Expected Salary")
    summary = fields.Text(string="Summary")
    expected_date = fields.Date(string="Expected Joining Date")
    stages = fields.Selection([('draft', 'Draft'), ('approve', 'Approved'), ('cancel', 'Cancel')],
                              default='draft')

    def approve_button(self):
        """Function to change stages to Approved on the click of button."""
        self.stages = 'approve'

    def create_application(self):
        return {'type': 'ir.actions.act_window',
                'res_model': 'product.template',
                'view_mode': 'form',
                'res_id': self.product_tmpl_id.id,
                'target': 'new'}
