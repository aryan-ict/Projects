"""This model is for Rent Management"""
from odoo import models, fields, api


class RentalManagement(models.Model):
    """This class is for fields And Required Function."""
    _name = "rental.management"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Model for Rent Management"

    name = fields.Char(string="Name", required=True)
    partner_id = fields.Many2one('res.partner', string="Customer")
    rental_type_id = fields.Many2one('rental.type', string="Rental Type")
    start_date = fields.Date(string="Start Date")
    end_date = fields.Date(string="End Date")
    rental_product = fields.Many2one('product.product',
                                     string="Rental Product")
    price = fields.Float(string="Price", related='rental_product.list_price')
    state = fields.Selection([('draft', 'Draft'), ('wait', 'Waiting'),
                              ('approve', 'Approve'), ('cancel', 'Cancel')],
                             default='draft', tracking=True)
    rent_ids = fields.Many2many('rental.type', 'rent_m2m_table', 'rental_management_id',
                                'rental_type_id', string="Rent")
    image_1920 = fields.Binary(string='Image')

    _sql_constraints = [
        ('check', 'CHECK((start_date <= end_date))', "End date must be greater then Start Date")
    ]

    @api.onchange('rental_type_id')
    def onchange_rental_type_id(self):
        """Function for Onchange Method."""
        for rec in self:
            print("rec-----", rec.rental_type_id.id)
            return {'domain': {'rental_product': [('rental_type_id', '=', rec.rental_type_id.id)]}}

    def product_button(self):
        pro = self.env['product.product'].search([('detailed_type', '=', 'service'), ('standard_price', '>', 20)],
                                                 order='create_date', limit=10)
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~products", pro)
