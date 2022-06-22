from odoo import models, fields, api, _


class PromotionalDiscount(models.Model):
    _name = "promotional.discount"
    _description = "Promotional Discount"

    discount_type = fields.Selection([('percentage', 'Percentage'), ('fixed', 'Fixed Amount')], string="Discount Type",
                                     required=True, default='percentage')
    name = fields.Char(string="Name")
    discount = fields.Float(string="Discount")
    minimum_order_amount = fields.Integer(string="Minimum Order Amount", default="100")
    start_date = fields.Datetime('Start Date')
    end_date = fields.Datetime('End Date')
    fixed_discount = fields.Monetary('Fixed Amount')
    currency_id = fields.Many2one('res.currency', default=20)

    _sql_constraints = [
        ('check', 'CHECK((start_date <= end_date))', "End Date must be greater than Start Date")
    ]
