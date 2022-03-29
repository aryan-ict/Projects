"""This module is for Smart View Tasks"""
from odoo import models, fields, api


# from odoo.exceptions import ValidationError


class SmartView(models.Model):
    """This Class is for fields and ORM Functions"""
    _name = "smart.view"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Model for Smart View"

    name = fields.Char(string="Name")
    name1 = fields.Char(string="Name1")
    email = fields.Char(string="Email", help="Enter your Email ID")
    address = fields.Text(string='Address')
    phone_no = fields.Char(string="Phone Number")
    doc = fields.Datetime(string="Date Of Creation",
                          default=lambda self: fields.Datetime.now())
    rating = fields.Selection([('bad', 'Bad'), ('good', 'Good'), ('best', 'Best'),
                               ('excellent', 'Excellent')], string='Rate Us')
    gender = fields.Selection([('male', 'Male'), ('female', 'Female'),
                               ('transgender', 'Transgender')],
                              string="Gender", tracking=True, default='male')
    status_bar = fields.Selection([('apply', 'Applied'),
                                   ('wait', 'Waiting'),
                                   ('approve', 'Approved')],
                                  default="apply",
                                  tracking=True)
    # names_list = fields.Many2one('college.management',
    #                              string="Name List")
    first_page_ids = fields.One2many('smart.view.otm', 'appointment_id',
                                     string='Appointment Lines')
    checkbox = fields.Boolean(string='Confirmed', help='Tick the Checkbox')
    rate_name = fields.Many2one('smart.view', string='Rated Names',
                                help="Names with 2 and more than 2 star rating",
                                domain=[('rating', '>=', 'best')])

    _sql_constraints = [
        ('name_uniq', 'unique (name)', "Name is already in the database.")
    ]

    def smart_button(self):
        """This function is for smart button"""
        self.unlink()
        return {
            'effect': {
                'fadeout': 'slow',
                'type': 'rainbow_man',
                'message': 'record updated'
            }
        }

    def log_button(self):
        """This function is for log button
        and posts a message in chatter on the click
        of the button and updates values.
        """
        up_vals = {'phone_no': '7575076690',
                   'gender': 'male'}
        self.message_post(body="Phone number has been updated "
                               "and Gender has been changed")
        self.write(up_vals)

    @api.model
    def create(self, vals):
        """Function for Create button and overriding using super function.
        When status of record is approve then checkbox will be checked.
        """
        res = super(SmartView, self).create(vals)
        print("res : ", res, "self", self, "vals", vals)
        res['name1'] = res['name']
        return res

    def write(self, vals):
        """Function for Edit button and overriding using super function."""
        res = super(SmartView, self).write(vals)
        print("res : ", res, "self", self, "vals", vals)
        if vals.get('status_bar') == 'approve':
            self['checkbox'] = 'True'
            print("Checkbox checked", self['checkbox'])
        return res

    def search_button(self):
        """Search Button function will get the name."""
        search_var = self.search([])
        print("search----", search_var)
        for rec in search_var:
            print("full_name...................", rec.name)

    @api.model
    def default_get(self, fields):
        """Function for Default Get Method"""
        res = super(SmartView, self).default_get(fields)
        print("fields----\n", fields)
        print("res----\n", res)
        res['gender'] = 'female'
        return res

    # @api.constrains('name')
    # def check_name(self):
    #     """Function to raise validation error on name field,
    #     If name contains any numeric value it will raise error."""
    #     for rec in self:
    #         if rec.name.isalpha() == False:
    #             raise ValidationError("Name must contain only alphabets")

    # @api.constrains('phone_no')
    # def check_number(self):
    #     """Function to raise validation error on phone field,
    #     If the length of phone number < or > 10 is will raise error."""
    #     for record in self:
    #         if len(record.phone_no) == 10:
    #             raise ValidationError("The number must be 10 digits long")

    def specialOperator(self):
        res = self.write({'first_page_ids': [(0, 0, {'product_qty': 999})]})

    def specialOperator_2(self):
        vals = {'first_page_ids': []}
        print("----------------------", vals)
        for rec in self.first_page_ids:
            print("---------------------", self.first_page_ids)
            vals['first_page_ids'].append([1, rec.id, {'product_qty': 159753}])
        self.write(vals)


class SmartViewOtm(models.Model):
    """This class is for One2many field"""
    _name = "smart.view.otm"
    _description = "Smart View One2many"
    _rec_name = 'test_list'

    product_id = fields.Many2one('product.product', string='Product')
    product_qty = fields.Integer(string='Product Quantity')
    appointment_id = fields.Many2one('smart.view', string='Appointment ID')
    test_list = fields.Many2one('smart.view.otm', string='Test')

    def test(self):
        """Simple test function"""
        return self

    def test1(self):
        """Simple test function"""
        return self
