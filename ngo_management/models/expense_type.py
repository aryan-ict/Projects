from odoo import models ,fields

class ExpenseType(models.Model):
    _name = "expense.type"
    _description = "list of all the expenses"

    name = fields.Char(string='Expense Type:', required=True)
