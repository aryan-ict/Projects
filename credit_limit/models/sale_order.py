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
        print(">>>>>>>>>>>>>>>>>>>>>>>block", credit_value.block_score)
        print("------------------vals", vals.get('state'))
        print("-----------------self", self.state)
        sale_draft = self.search([('state', '=', 'draft'), ('partner_id', '=', vals.get('partner_id'))])
        sale_confirm = self.search([('state', '=', 'sale'), ('partner_id', '=', vals.get('partner_id'))])
        total_records = sale_draft + sale_confirm
        print("::::::::::::::::::::::::::::::::::confirm", sale_confirm)
        for rec in total_records:
            if rec.state in 'draft':
                sum_list.append(rec.amount_total)
                if credit_value.credit_limit:
                    if sum(sum_list) > credit_value.credit_score:
                        raise ValidationError("Your Sale Order Credit Limit has been Exceeded")
            elif rec.state in 'sale':
                sum_list.append(rec.amount_total)
                if credit_value.block_limit:
                    if sum(sum_list) > credit_value.block_score:
                        raise ValidationError("You cannot create SO as the Block Limit has been Exceeded")
            print("_____________________", sum_list)
            print("++++++++++++++++++++++++++sum", sum(sum_list))
        return res
