from odoo import models, fields, api, _


class ResConfigSetting(models.TransientModel):
    _inherit = "res.config.settings"
    _description = "Res Config Settings"

    group_covid_delivery_message = fields.Boolean("Display COVID delivery message",
                                                  implied_group="aryanmodh_29062022.group_aryanmodh_29062022")
