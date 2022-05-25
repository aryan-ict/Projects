from odoo import models, fields, api


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

    def progress_button(self):
        self.history_lines('progress')
        disp_msg = """Contact : """ + self.contact_id.name + """
        <br/>
        Sale Order : """ + self.sale_order_id.name

        self.message_post(body=disp_msg)

    def done_button(self):
        self.history_lines('done')
        self.message_post(body=[self.contact_id.name, self.sale_order_id.name])

    def cancel_button(self):
        self.history_lines('cancel')
        self.message_post(body=[self.contact_id.name, self.sale_order_id.name])

    def draft_button(self):
        self.history_lines('draft')
        self.message_post(body=[self.contact_id.name, self.sale_order_id.name])

    @api.model
    def create(self, vals):
        vals['name'] = self.env['ir.sequence'].next_by_code('contact.sale')
        return super(ContactSale, self).create(vals)

    def history_lines(self, status):
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
    _name = "contact.sale.history"
    _description = "Model for Contact Sale History"

    contact_sale_id = fields.Many2one('contact.sale')
    old_state = fields.Char("Old State")
    new_state = fields.Char("New State")
    old_follow_up = fields.Integer("Old No. of Follow Ups")
    new_follow_up = fields.Integer("New No. of Follow Ups")
