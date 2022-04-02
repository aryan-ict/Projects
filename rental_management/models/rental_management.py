"""This model is for Rent Management"""
from odoo import models, fields, api


class RentalManagement(models.Model):
    """This class is for fields"""
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

    @api.onchange('rental_type_id')
    def onchange_rental_type_id(self):
        """Function for Onchange Method."""
        for rec in self:
            print("rec-----", rec.rental_type_id.id)
            return {'domain': {'rental_product': [('rental_type_id', '=', rec.rental_type_id.id)]}}

    def get_data(self):
        """Function for read method.
        :return: List of Dictionary"""
        res = self.env['res.partner'].search([]).read([])
        return res

    def get_data_email(self):
        """Function to get all the email of res.partner."""
        rec = self.env['res.partner'].search([]).read(['email'])
        for res in rec:
            print(res)

    # Output:
    # {'id': 14, 'email': 'azure.Interior24@example.com'}
    # {'id': 26, 'email': 'brandon.freeman55@example.com'}
    # {'id': 33, 'email': 'colleen.diaz83@example.com'}
    # {'id': 27, 'email': 'nicole.ford75@example.com'}
    # {'id': 10, 'email': 'deco.addict82@example.com'}
    # {'id': 35, 'email': 'addison.olson28@example.com'}
    # {'id': 18, 'email': 'douglas.fletcher51@example.com'}
    # {'id': 19, 'email': 'floyd.steward34@example.com'}
    # {'id': 11, 'email': 'gemini.furniture39@example.com'}
    # {'id': 20, 'email': 'edwin.hansen58@example.com'}
    # {'id': 22, 'email': 'jesse.brown74@example.com'}
    # {'id': 31, 'email': 'oscar.morgan11@example.com'}
    # {'id': 23, 'email': 'soham.palmer15@example.com'}
    # {'id': 15, 'email': 'lumber-inv92@example.com'}
    # {'id': 34, 'email': 'lorraine.douglas35@example.com'}
    # {'id': 42, 'email': 'demo@yourcompany.example.com'}
    # {'id': 41, 'email': 'admin@yourcompany.example.com'}
    # {'id': 12, 'email': 'ready.mat28@example.com'}
    # {'id': 21, 'email': 'billy.fox45@example.com'}
    # {'id': 25, 'email': 'edith.sanchez68@example.com'}
    # {'id': 37, 'email': 'julie.richards84@example.com'}
    # {'id': 24, 'email': 'kim.snyder96@example.com'}
    # {'id': 36, 'email': 'sandra.neal80@example.com'}
    # {'id': 30, 'email': 'theodore.gardner36@example.com'}
    # {'id': 38, 'email': 'travis.mendoza24@example.com'}
    # {'id': 13, 'email': 'jackson.group82@example.com'}
    # {'id': 29, 'email': 'gordon.owens47@example.com'}
    # {'id': 28, 'email': 'toni.rhodes11@example.com'}
    # {'id': 9, 'email': 'wood.corner26@example.com'}
    # {'id': 17, 'email': 'ron.gibson76@example.com'}
    # {'id': 32, 'email': 'tom.ruiz89@example.com'}
    # {'id': 16, 'email': 'willie.burke80@example.com'}
    # {'id': 1, 'email': 'info@yourcompany.com'}
    # {'id': 39, 'email': 'chester.reed79@example.com'}
    # {'id': 40, 'email': 'dwayne.newman28@example.com'}
    # {'id': 8, 'email': 'joel.willis63@example.com'}
    # {'id': 7, 'email': 'mark.brown23@example.com'}
    # {'id': 3, 'email': 'admin@yourcompany.example.com'}
    # {'id': 51, 'email': False}
    # {'id': 50, 'email': False}

    def get_email_true(self):
        """Function to get email which are not False."""
        rec = self.env['res.partner'].search_read([('email', '!=', False)], ['email'])
        for res in rec:
            print(res)

    # Output:
    # {'id': 14, 'email': 'azure.Interior24@example.com'}
    # {'id': 26, 'email': 'brandon.freeman55@example.com'}
    # {'id': 33, 'email': 'colleen.diaz83@example.com'}
    # {'id': 27, 'email': 'nicole.ford75@example.com'}
    # {'id': 10, 'email': 'deco.addict82@example.com'}
    # {'id': 35, 'email': 'addison.olson28@example.com'}
    # {'id': 18, 'email': 'douglas.fletcher51@example.com'}
    # {'id': 19, 'email': 'floyd.steward34@example.com'}
    # {'id': 11, 'email': 'gemini.furniture39@example.com'}
    # {'id': 20, 'email': 'edwin.hansen58@example.com'}
    # {'id': 22, 'email': 'jesse.brown74@example.com'}
    # {'id': 31, 'email': 'oscar.morgan11@example.com'}
    # {'id': 23, 'email': 'soham.palmer15@example.com'}
    # {'id': 15, 'email': 'lumber-inv92@example.com'}
    # {'id': 34, 'email': 'lorraine.douglas35@example.com'}
    # {'id': 42, 'email': 'demo@yourcompany.example.com'}
    # {'id': 41, 'email': 'admin@yourcompany.example.com'}
    # {'id': 12, 'email': 'ready.mat28@example.com'}
    # {'id': 21, 'email': 'billy.fox45@example.com'}
    # {'id': 25, 'email': 'edith.sanchez68@example.com'}
    # {'id': 37, 'email': 'julie.richards84@example.com'}
    # {'id': 24, 'email': 'kim.snyder96@example.com'}
    # {'id': 36, 'email': 'sandra.neal80@example.com'}
    # {'id': 30, 'email': 'theodore.gardner36@example.com'}
    # {'id': 38, 'email': 'travis.mendoza24@example.com'}
    # {'id': 13, 'email': 'jackson.group82@example.com'}
    # {'id': 29, 'email': 'gordon.owens47@example.com'}
    # {'id': 28, 'email': 'toni.rhodes11@example.com'}
    # {'id': 9, 'email': 'wood.corner26@example.com'}
    # {'id': 17, 'email': 'ron.gibson76@example.com'}
    # {'id': 32, 'email': 'tom.ruiz89@example.com'}
    # {'id': 16, 'email': 'willie.burke80@example.com'}
    # {'id': 1, 'email': 'info@yourcompany.com'}
    # {'id': 39, 'email': 'chester.reed79@example.com'}
    # {'id': 40, 'email': 'dwayne.newman28@example.com'}
    # {'id': 8, 'email': 'joel.willis63@example.com'}
    # {'id': 7, 'email': 'mark.brown23@example.com'}
    # {'id': 3, 'email': 'admin@yourcompany.example.com'}

    def get_data_name(self):
        """Function the get record name on the bases of their ids"""
        print(self.env['res.partner'].browse([3, 15]).read(['name']))
    # Output: [{'id': 3, 'name': 'Mitchell Admin'}, {'id': 15, 'name': 'Lumber Inc'}]
