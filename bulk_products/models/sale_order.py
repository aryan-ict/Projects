from odoo import models, fields, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'
    _description = 'Inherit Sale Order'

    bulk_product_template_id = fields.Many2one('bulk.products', string='Bulk Product Template')

    @api.onchange('bulk_product_template_id')
    def _onchange_bulk_product(self):
        bulk_ids = self.env['bulk.products'].browse(self.bulk_product_template_id.id)
        print("-------------------------", bulk_ids)
        new_lines = []
        for res in bulk_ids.bulk_product_ids:
            new_lines.append((0, 0, {
                'product_id': res.product_id.id,
                'name': res.product_id.name,
                'product_uom_qty': res.product_uom_qty,
                'product_uom': res.product_id.uom_id.id

            }))
            print("========================", new_lines)
        self.update({
            'order_line': new_lines,
            'partner_invoice_id': self.partner_id.id,
        })
