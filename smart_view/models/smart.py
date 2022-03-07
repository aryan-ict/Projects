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
    phone_no = fields.Char(string="Phone Number",
                           related='names_list.mobile_no')
    doc = fields.Datetime(string="Date Of Creation",
                          default=lambda self: fields.Datetime.now())
    rating = fields.Selection([('bad', 'Bad'), ('good', 'Good'), ('best', 'Best'),
                               ('excellent', 'excellent')], string='Rate Us')
    gender = fields.Selection([('male', 'Male'), ('female', 'Female'),
                               ('transgender', 'Transgender')],
                              string="Gender", tracking=True)
    status_bar = fields.Selection([('apply', 'Applied'),
                                   ('wait', 'Waiting'),
                                   ('approve', 'Approved')],
                                  default="apply",
                                  tracking=True)
    names_list = fields.Many2one('college.management',
                                 string="Name List")
    first_page = fields.One2many('smart.view.otm', 'appointment_id',
                                 string='Appointment Lines')
    checkbox = fields.Boolean(string='Confirmed', help='Tick the Checkbox')

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
        search_var = self.search([])
        print("search----", search_var)
        for rec in search_var:
            print("full_name...................", rec.name)


# @api.constrains('name')
# def check_name(self):
#     for rec in self:
#         if rec.name.isalpha() == False:
#             raise ValidationError("Name must contain only alphabets")

# @api.constrains('phone_no')
# def check_number(self):
#     for record in self:
#         if len(record.phone_no) > 10 or len(record.phone_no) < 10:
#             raise ValidationError("The number must be 10 digits long")


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
