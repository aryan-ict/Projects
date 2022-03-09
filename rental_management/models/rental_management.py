"""This model is for Rent Management"""
from odoo import models, fields, api


class RentalManagement(models.Model):
    """This class is for fields"""
    _name = "rental.management"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Model for Rent Management"

    name = fields.Char(string="Name")
    partner_id = fields.Many2one('res.partner', string="Customer")
    rental_type_id = fields.Many2one('rental.type',string="Rental Type")
    start_date = fields.Datetime(string="Start Date")
    end_date = fields.Datetime(string="End Date", readonly=True)
    rental_product = fields.Many2one('product.product', string="Rental Product")
    price = fields.Float(string="Price", related='rental_product.list_price')
    state = fields.Selection([('draft', 'Draft'), ('wait', 'Waiting'),
                              ('approve', 'Approve'), ('cancel', 'Cancel')],
                             default='draft', tracking=True)
