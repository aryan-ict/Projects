from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class SaleOrder(models.Model):
    _inherit = "sale.order"
    _description = "Sale Order"

    @api.model
    def create(self, vals):
        sum_list = []
        res = super(SaleOrder, self).create(vals)
        credit_value = self.env['res.partner'].search([('id', '=', vals.get('partner_id'))])
        print(">>>>>>>>>>>>>>>>>>>>>>>credit", credit_value.credit_score)
        print("------------------vals", vals)
        # print("-----------------", self.search([('state', '=', 'draft')]))
        sale_draft = self.search([('state', '=', 'draft'), ('partner_id', '=', vals.get('partner_id'))])
        sale_confirm = self.search([('state', '=', 'sale'), ('partner_id', '=', vals.get('partner_id'))])
        print("::::::::::::::::::::::::::::::::::confirm", sale_confirm)
        if self.state == 'draft':
            for rec in sale_draft:
                sum_list.append(rec.amount_total)
                print("_____________________", sum_list)
                print("++++++++++++++++++++++++++sum", sum(sum_list))
                if credit_value.credit_limit:
                    if sum(sum_list) > credit_value.credit_score:
                        raise ValidationError("Your Sale Order Credit Limit has been Exceeded")
        elif self.state == 'sale':
            for rec in sale_confirm:
                sum_list.append(rec.amount_total)
                if credit_value.block_limit:
                    if sum(sum_list) > credit_value.block_score:
                        raise ValidationError("You cannot create SO as the Block Limit has been Exceeded")
        return res
