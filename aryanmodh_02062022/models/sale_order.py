from odoo import models, fields, api


class SaleOrder(models.Model):
    _inherit = "sale.order"
    _description = "Sale Order"

    @api.model
    def _search(self, args, offset=0, limit=None, order=None, count=False, access_rights_uid=None):
        context = self._context
        print("------------------------context", context)
        print("---------------------self", self)
        print("=====================args", args)
        if context.get('operation_type'):
            if context.get('operation_type') in 'confirm':
                args = [('state', 'in', ['draft', 'sent']), ('user_id', '=', context.get('responsible_id'))]
            elif context.get('operation_type') in 'cancel':
                args = [('state', 'in', ['draft', 'sent', 'sale']), ('user_id', '=', context.get('responsible_id'))]
            elif context.get('operation_type') in 'merge':
                args = [('state', 'in', ['draft', 'sent']), ('user_id', '=', context.get('responsible_id')),
                        ('partner_id', '=', context.get('partner_id'))]

        return super(SaleOrder, self)._search(args, offset=0, limit=None, order=None, count=False,
                                              access_rights_uid=None)
