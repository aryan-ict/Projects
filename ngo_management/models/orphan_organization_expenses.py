from odoo import models, fields,api


class OrganizationExpense(models.Model):
    _name = "orphans.organization.expense"
    _description = "All orphan expenses are recorded here."

    expense_user = fields.Char(string="Name", help="Spender name..!", required=True)
    expense_type_id = fields.Many2one("expense.type",string="Expense type",required=True)
    currency_id = fields.Many2one("res.currency",
                                  string="Currency",
                                  default=20)
    expense_amount = fields.Monetary(string="Expense Amount", required=True)
    organization_id = fields.Many2one(comodel_name='orphans.organization', string="Orphans Home",required=True)
    ngo_id = fields.Many2one(string="Ngo",
                             related="organization_id.ngo_id")
    notes = fields.Text(string="Notes")

    # @api.model_create_multi
    # def create(self, vals):
    #     print("\n\nFUnction Called\n\n")
    #     res_id = super(OrganizationExpense, self).create(vals)
    #     org = self.env["res.partner"]
    #
    #     for rec in vals:
    #         print("loop run")
    #         print(rec['expense_amount'])
    #         if rec['expense_amount']:
    #             print('if True\n\n')
    #             amount = rec['expense_amount']
    #             organization_id = org.browse(rec['name'])
    #             print("\n\n\n Available Funds: \
    #                    {}".format(organization_id.amount))
    #             organization_id.amount -= amount
    #             print(" Updated Funds: {}, \
    #                    Expense: {}".format(organization_id.amount, amount), "\n")
    #     return res_id