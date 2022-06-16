from odoo import models, fields, api


class BatchWizard(models.TransientModel):
    _name = "batch.wizard"
    _description = "Batch Wizard"

    sale_order_ids = fields.One2many('batch.wizard.line', 'batch_wizard_id', string="Sale Order")

    @api.model
    def default_get(self, fields):
        new_line = []
        res = super(BatchWizard, self).default_get(fields)
        rec = self.env['batch.sale.workflow'].browse(self.env.context.get('active_id'))
        print("-----------------------res", res)
        print("=======================rec", rec.sale_order_ids.order_line)
        print("+++++++++++++++++++++++fields", fields)
        for line in rec.sale_order_ids.order_line:
            new_line.append((0, 0, {
                'product_id': line.product_id.id,
                'description': line.name,
                'product_qty': line.product_uom_qty,
                'price_unit': line.price_unit
            }))
        print("------------------->>>>>>new_line", new_line)
        res.update({
            'sale_order_ids': new_line
        })
        return res

    def submit_btn(self):
        new_order_line = []
        for line in self.sale_order_ids:
            new_order_line.append((0, 0, {
                'product_id': line.product_id.id,
                'product_uom_qty': line.product_qty,
                'price_unit': line.price_unit
            }))
        print("--------------------------Hello World", new_order_line)

        for rec in self.env['batch.sale.workflow'].browse(self.env.context.get('active_ids')):
            print("-------------------parnter", rec)
            self.env['sale.order'].create({
                'partner_id': rec.partner_id.id,
                'order_line': new_order_line
            })


class BatchWizardLine(models.TransientModel):
    _name = "batch.wizard.line"
    _description = "Batch Wizard Line"

    product_id = fields.Many2one('product.product', string="Product")
    description = fields.Text(string="Description")
    product_qty = fields.Float(string="Product Quantity")
    price_unit = fields.Float(string="Unit Price")
    batch_wizard_id = fields.Many2one('batch.wizard')
