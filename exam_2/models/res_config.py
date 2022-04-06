"""This model is for Config settings."""
from odoo import models, fields, api
from ast import literal_eval


class ResConfigSetting(models.TransientModel):
    """This class inherits res.config.settings"""
    _inherit = 'res.config.settings'

    module_advance_action = fields.Boolean(string="Install")
    filter_order_ids = fields.Many2many('sale.order', string="Orders")

    @api.model
    def set_values(self):
        """Function to set values.
        ":return:Record Set"""
        res = super(ResConfigSetting, self).set_values()
        self.env['ir.config_parameter'].set_param('exam_2.filter_order_ids', self.filter_order_ids.ids)
        return res

    @api.model
    def get_values(self):
        """Function to get values.
        :return:Record Set"""
        res = super(ResConfigSetting, self).get_values()
        filter_save = self.env['ir.config_parameter'].get_param('exam_2.filter_order_ids')
        res.update(
            filter_order_ids=[(6, 0, literal_eval(filter_save))])
        return res
