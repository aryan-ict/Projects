from odoo import models, fields, api
from dateutil.relativedelta import relativedelta
import datetime


class ContactSale(models.Model):
    _name = "contact.sale"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Model for Contact Sale"

    name = fields.Char("Name", readonly=True)
    contact_id = fields.Many2one('res.partner', string="Contact")
    sale_order_id = fields.Many2one('sale.order', string="Sale Order", domain="[('partner_id', '=', contact_id)]")
    user_id = fields.Many2one('res.users', string="Sales Person", related='sale_order_id.user_id', store=True)
    state = fields.Selection([('draft', 'Draft'), ('progress', 'In Progress'),
                              ('done', 'Done'), ('cancel', 'Cancel')], default="draft", tracking=True)
    follow_ups = fields.Integer("No. of Follow Ups")
    contact_sale_history_ids = fields.One2many('contact.sale.history', 'contact_sale_id',
                                               string="Contact Sale History Lines", readonly=True)
    birth_date = fields.Date()
    age = fields.Integer(compute="_compute_birth_age")

    @api.depends('birth_date')
    def _compute_birth_age(self):
        """Function to Compute age using relativedelta."""
        today_date = datetime.date.today()
        print("-----------------------------", today_date)
        print("=============================", self.birth_date)
        if self.birth_date:
            print("--------------------birth date", self.birth_date)
            age1 = relativedelta(today_date, self.birth_date).years
            self.age = age1
            print("++++++++++++++++++++++++++", self.age)
        else:
            self.age = 0

    def progress_button(self):
        """Function for progress button,
        On the click of button state will change to In progress."""
        self.history_lines('progress')
        self.message_post(body=[self.contact_id.name, self.sale_order_id.name])

    def done_button(self):
        """Function for done button,
        On the click of button state will change to Done."""
        self.history_lines('done')
        self.message_post(body=[self.contact_id.name, self.sale_order_id.name])

    def cancel_button(self):
        """Function for cancel button,
        On the click of button state will change to Cancel."""
        self.history_lines('cancel')
        self.message_post(body=[self.contact_id.name, self.sale_order_id.name])

    def draft_button(self):
        """Function for draft button,
        On the click of button state will change to Draft."""
        self.history_lines('draft')
        self.message_post(body=[self.contact_id.name, self.sale_order_id.name])

    @api.model
    def create(self, vals):
        """Function to create sequential name, using ir.sequence."""
        vals['name'] = self.env['ir.sequence'].next_by_code('contact.sale')
        return super(ContactSale, self).create(vals)

    def history_lines(self, status):
        """Function for history lines which will be auto-generated,
        On the click of any state button."""
        print("===============------------>>>>>>>>>>>", status)
        old_state = self.state
        old_follow_up = self.follow_ups
        print("=================================", old_state, old_follow_up)
        self.follow_ups += 1
        new_follow_up = self.follow_ups
        self.state = status
        new_state = self.state
        print("------------------------------", new_follow_up, new_state)
        lines_data = {
            'old_state': old_state,
            'new_state': new_state,
            'old_follow_up': old_follow_up,
            'new_follow_up': new_follow_up
        }
        self.write({
            'contact_sale_history_ids': [(0, 0, lines_data)]
        })


class ContactSaleHistory(models.Model):
    """Model for One2many field."""
    _name = "contact.sale.history"
    _description = "Model for Contact Sale History"

    contact_sale_id = fields.Many2one('contact.sale')
    old_state = fields.Char("Old State")
    new_state = fields.Char("New State")
    old_follow_up = fields.Integer("Old No. of Follow Ups")
    new_follow_up = fields.Integer("New No. of Follow Ups")
