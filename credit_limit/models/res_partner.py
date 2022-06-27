from odoo import models, fields, api, _


class ResPartner(models.Model):
    _inherit = "res.partner"
    _description = "Contacts"

    credit_limit = fields.Boolean('Credit Limit')
    credit_score = fields.Float('Credit Limit Score')
    block_limit = fields.Boolean('Blocking Limit')
    block_score = fields.Float('Blocking Limit Score')
