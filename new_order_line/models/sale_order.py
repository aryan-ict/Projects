from odoo import models, fields, api, _
from odoo.exceptions import UserError


class SaleOrder(models.Model):
    _inherit = "sale.order"
    _description = "Sale Order"

    new_order_line_ids = fields.One2many('new.order.line', 'sale_order_id')

    @api.model
    def create(self, vals):
        res = super(SaleOrder, self).create(vals)
        res.merge_sale_order_line()
        return res

    def write(self, vals):
        """Override write function which will add Sale Order Line
        into a new One2many field name New Order Line."""
        res = super(SaleOrder, self).write(vals)
        self.merge_sale_order_line()
        return res

    def merge_sale_order_line(self):
        for rec in self.order_line.mapped("product_id"):
            line_ids = self.order_line.filtered(lambda m: m.product_id.id == rec.id)
            price = line_ids.mapped("price_unit")
            new_line = []
            for res in line_ids:
                if res.price_unit != price[0]:
                    raise UserError('Unit Price Must be Same.')
                else:
                    pass
            quantity = line_ids.mapped("product_uom_qty")
            subtotal = line_ids.mapped("price_subtotal")
            print("---------------rec", rec)
            print("---------------line_ids", line_ids)
            print("---------------quantity", sum(quantity))
            print("---------------price_unit", price)
            print("---------------subtotal", subtotal)
            new_line.append((0, 0, {
                'product_id': rec.id,
                'name': rec.name,
                'product_uom_qty': sum(quantity),
                'price_unit': price[0],
                'price_subtotal': sum(subtotal)
            }))
            if rec not in self.new_order_line_ids.product_id:
                self.write({
                    'new_order_line_ids': new_line
                })
                print("-------------With Context", self._context)
            # elif rec in self.new_order_line_ids.product_id:
            #     for line in self.env['new.order.line']:
            #         print("---------------line", line)
            #         self.write({
            #             'new_order_line_ids': [(1, line.id, {
            #                 'product_uom_qty': sum(quantity),
            #                 'price_subtotal': sum(subtotal)
            #             })]
            #         })


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"
    _description = "Sale Order Line"

    def unlink(self):
        """Unlink function to unlink the selected record based on Sale Order Line,
        When record is deleted from Sale Order Line then it will be deleted from
        New Order Line."""
        for vals in self.mapped("product_id"):
            rec = self.filtered(lambda m: m.product_id.id == vals.id)
            new_line_id = self.env['new.order.line'].filtered(lambda x: x.product_id.id == vals.id)
            print("-----------------new_line_id", new_line_id)
            print("-----------------rec vals : ", vals)
            print("-----------------rec", rec)
            # print("-----------------With Context", self.with_context(printed=True))
            # rec.unlink()
        return super(SaleOrderLine, self).unlink()
