from odoo import models, fields, api


class BulkProduct(models.Model):
    _name = "bulk.products"
    _description = "Model for Bulk Products"

    name = fields.Char(string='Name', required=True)
    master_id = fields.Many2one('product.template', string='Master Product')
    bulk_product_ids = fields.One2many('bulk.product.line', 'bulk_id',  string='Bulk Product')
    user_id = fields.Many2one('res.partner', string='User')
    email = fields.Char(string='Email')
    bulk_id = fields.Many2one('bulk.products', string='Bulk')

    @api.model
    def create(self, vals):
        print("---------------------------values", vals)
        return super(BulkProduct, self).create(vals)

    def write(self, vals):
        print("============================values", vals)
        return super(BulkProduct, self).write(vals)


class BulkProductLine(models.Model):
    _name = "bulk.product.line"
    _description = "Bulk Product Line"

    product_id = fields.Many2one('product.product', string='Products')
    description = fields.Char(string='Description', related='product_id.name')
    product_uom_qty = fields.Float(string='Quantity', default='1.00')
    bulk_id = fields.Many2one('bulk.products')
