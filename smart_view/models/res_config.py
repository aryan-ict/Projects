"""This model is for Config Setting."""
from odoo import models, fields, api


class ResConfigSetting(models.TransientModel):
    """This class is for Field inheritance."""
    _inherit = 'res.config.settings'
    _description = "Settings Inheritance"

    check_box = fields.Boolean(string="Check Box", config_parameter="smart_view.check_box")
    test_html = fields.Char(string="Html Field", config_parameter="smart_view.test_html")
    compan_id = fields.Many2one('res.company', string="Company", config_parameter="smart_view.compan_id")

    # @api.model
    # def get_value(self):
    #     """Function to get values in config setting.
    #     :return: Record Set"""
    #     res = super(ResConfigSetting, self).get_value()
    #     res['test_html'] = self.env['ir.config_parameter'].get_param(
    #         'test_html')
    #     return res

    # @api.model
    # def set_values(self):
    #     """Function to set values in config setting."""
    #     self.env['ir.config_parameter'].set_param(
    #         'test_html', self.test_html)
    #     super(ResConfigSetting, self).set_values()

    @api.onchange('check_box')
    def _onchange_checkbox(self):
        """Function to change values of fields when
        check box is unchecked."""
        for rec in self:
            if not rec.check_box:
                rec.test_html = False
                rec.compan_id = False
