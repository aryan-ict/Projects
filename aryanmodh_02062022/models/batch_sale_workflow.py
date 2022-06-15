from odoo import models, fields, api
import datetime


class BatchSaleWorkflow(models.Model):
    _name = "batch.sale.workflow"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Batch Sale Workflow"

    name = fields.Char('Name', readonly=True)
    responsible_id = fields.Many2one('res.users', string='Responsible', tracking=True)
    operation_type = fields.Selection([('confirm', 'Confirm'), ('cancel', 'Cancel'), ('merge', 'Merge')],
                                      default='confirm', string='Operation Type')
    partner_id = fields.Many2one('res.partner', string='Customer')
    status = fields.Selection([('draft', 'Draft'), ('done', 'Done'), ('cancel', 'Cancel')], default='draft',
                              tracking=True)
    sale_order_ids = fields.Many2many('sale.order', 'sale_order_rel', 'batch_sale_id', 'sale_order_id',
                                      string='Sale Order')
    operation_date = fields.Datetime('Operation Date')

    @api.model
    def create(self, vals):
        """Function to create sequential name, using ir.sequence."""
        print("-------------------------", vals)
        vals['name'] = self.env['ir.sequence'].next_by_code('batch.sale.workflow')
        return super(BatchSaleWorkflow, self).create(vals)

    def write(self, vals):
        print("==========================", vals)
        return super(BatchSaleWorkflow, self).write(vals)

    def proceed_ops_button(self):
        """Function for proceed operation button,
        On the click of button state will change to done and date will
        added to order date field in sale order if the condition is true."""
        self.status = 'done'
        res = self.env['sale.order']
        if self.operation_type in 'confirm':
            self.sale_order_ids.write({
                'date_order': self.operation_date
            })
            self.sale_order_ids.action_confirm()
        elif self.operation_type in 'cancel':
            self.sale_order_ids.action_cancel()
        elif self.operation_type in 'merge':
            print("------------------------order_line", self.sale_order_ids.order_line)
            self.sale_order_ids.action_cancel()
            res.create({
                'partner_id': self.partner_id.id,
                'order_line': self.sale_order_ids.order_line
            })

    def cancel_button(self):
        """Function for cancel button,
        On the click of button state will change to cancel."""
        self.status = 'cancel'

    def draft_button(self):
        """Function for draft button,
        On the click of button state will change to draft."""
        self.status = 'draft'

    @api.onchange('responsible_id', 'operation_type', 'partner_id')
    def _onchange_operation_type(self):
        """Onchange function to get values based of on
        the given domain."""
        for rec in self:
            if rec.operation_type in 'confirm':
                domain = [('state', 'in', ['draft', 'sent']), ('user_id', '=', rec.responsible_id.id)]

            elif rec.operation_type in 'cancel':
                domain = [('state', 'in', ['draft', 'sent', 'sale']), ('user_id', '=', rec.responsible_id.id)]

            elif rec.operation_type in 'merge':
                domain = [('state', 'in', ['draft', 'sent']), ('user_id', '=', rec.responsible_id.id),
                          ('partner_id', '=', rec.partner_id.id)]
        return {'domain': {'sale_order_ids': domain}}
