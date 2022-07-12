from odoo import models, fields, api, _


class SaleOrder(models.Model):
    _inherit = "sale.order"
    _description = "Sale Order"

    new_order_line_ids = fields.One2many('new.order.line', 'sale_order_id')

    # def write(self, vals):
    #     """Override write function which will add Sale Order Line
    #     into a new One2many field name New Order Line."""
    #     res = super(SaleOrder, self).write(vals)
    #     self.merge_sale_order_line()
    #     return res
    #     for rec in self.order_line:
    #         if rec not in self.new_order_line_ids.order_line_id:
    #             self.env['new.order.line'].create({
    #                 'order_line_id': rec.id,
    #                 'product_id': rec.product_id.id,
    #                 'name': rec.name,
    #                 'product_uom_qty': rec.product_id.id,
    #                 'price_unit': rec.price_unit,
    #                 'price_subtotal': rec.price_subtotal,
    #                 'sale_order_id': self.id
    #             })
    #     return res

    def merge_sale_order_line(self):
        for rec in self.order_line:
            if rec.id in self.order_line.ids:
                line_ids = self.order_line.mapped(lambda m: m.product_id.id)
                # new_line_ids = self.new_order_line_ids.filtered(lambda m: m.product_id.id == rec.product_id.id)
                # print("===============New Line Ids", new_line_ids)
                print("---------------Line Ids : ", line_ids)
            #     quantity = 0
            #     for qty in line_ids:
            #         print("--------------Quantity : ", qty)
            #         quantity += qty.product_uom_qty
            #         subtotal = qty.price_unit * quantity
            #         print("______________Product QTY : ", quantity)
            #
            if rec not in self.new_order_line_ids.order_line_id:
                self.env['new.order.line'].create({
                    'product_id': line_ids[0],
                    'name': rec.name,
                    'product_uom_qty': rec.product_uom_qty,
                    'price_unit': rec.price_unit,
                    'price_subtotal': rec.price_subtotal,
                    'sale_order_id': self.id
                })
                # new_line_ids[:-1].unlink()


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"
    _description = "Sale Order Line"

    def unlink(self):
        """Unlink function to unlink the selected record based on Sale Order Line,
        When record is deleted from Sale Order Line then it will be deleted from
        New Order Line."""
        for vals in self:
            rec = self.env['new.order.line'].search([('order_line_id', '=',
                                                      vals.id)])  # Here it will search for records in new order line whose order_line_id = to self.id
            print("-----------------rec vals : ", vals)
            rec.unlink()
        return super(SaleOrderLine, self).unlink()
