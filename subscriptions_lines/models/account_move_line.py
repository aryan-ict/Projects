"""This model is for Invoicing."""
from odoo import models, fields, api


class AccountMoveLine(models.Model):
    """This class is for fields inherited in Invoice Lines."""
    _inherit = 'account.move.line'
    _description = 'Invoice Lines'
    _rec_name = 'name'

    delivery_add_id = fields.Many2one('res.partner', string="Delivery Address", domain=[('type', '=', 'delivery')])
    vendor_id = fields.Many2one('res.partner', string="Vendor", domain=[('supplier_rank', '>', 0)])
    vendor_price = fields.Float(string="Vendor Price")
    planned_gp = fields.Float(string="Planned GP%")
    description = fields.Text(string="Description", compute="_compute_description")

    @api.onchange('vendor_price', 'price_unit')
    def _onchange_planned_gp(self):
        for rec in self:
            if rec.vendor_price or rec.price_unit:
                rec.planned_gp = ((rec.price_unit - rec.vendor_price)/rec.price_unit)*100
                print("-----------------------", rec.planned_gp)

    @api.depends('delivery_add_id', 'name')
    def _compute_description(self):
        for rec in self:
            if rec.delivery_add_id and rec.name:
                rec.description = rec.delivery_add_id.name + ", " + rec.name
            else:
                rec.description = "Add Description"
