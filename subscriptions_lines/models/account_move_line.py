"""This model is for Invoicing."""
from odoo import models, fields, api


class AccountMoveLine(models.Model):
    """This class is for fields inherited in Invoice Lines."""
    _inherit = 'account.move.line'
    _description = 'Invoice Lines'

    delivery_add_id = fields.Many2one('res.partner', string="Delivery Address")
    vendor_id = fields.Many2one('res.partner', string="Vendor",
                                domain=[('supplier_rank', '>', 0), ('type', '=', 'contact')])
    vendor_price = fields.Float(string="Vendor Price")
    planned_gp = fields.Float(string="Planned GP%")
    description = fields.Html(string="Description", compute="_compute_description")

    @api.onchange('vendor_price', 'price_unit')
    def _onchange_planned_gp(self):
        """Function to calculate planned_gp Onchange of vendor_price OR price_unit."""
        for rec in self:
            if rec.vendor_price or rec.price_unit:
                rec.planned_gp = ((rec.price_unit - rec.vendor_price) / rec.price_unit) * 100
                print("-----------------------", rec.planned_gp)

    @api.depends('delivery_add_id', 'product_id')
    def _compute_description(self):
        """Function to concatenate Delivery Address and Label field in Description field."""
        print("---------------------------", self._context)
        for rec in self:
            if rec.delivery_add_id and rec.product_id:
                rec.description = rec.delivery_add_id.name + ", " + str(rec.product_id.description)
            else:
                rec.description = "Add Description"
