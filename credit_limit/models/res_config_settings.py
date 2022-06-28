from odoo import models, fields, api, _


class ResConfigSetting(models.TransientModel):
    _inherit = "res.config.settings"
    _description = "Res Config Settings"

    notify_email = fields.Char("Notify Person for limit Exceed", config_parameter="credit_limit.notify_email")
