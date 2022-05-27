from odoo import models, fields, api


class ResPartner(models.Model):
    _inherit = "res.partner"
    _description = "Model for Inheritance of Contact"

    contact_sale_count = fields.Integer(compute='compute_contact_sale')

    def compute_contact_sale(self):
        for rec in self:
            domain = [('contact_id', '=', rec.id)]
            contact_sale = self.env['contact.sale'].search(domain)
            print("--------------------", contact_sale)
            rec.contact_sale_count = len(contact_sale)
            if len(contact_sale) > 1:
                view = 'tree,form'
            else:
                view = 'form'
        return {
            'name': 'Contact Sale Action',
            'view_mode': view,
            'res_model': 'contact.sale',
            'res_id': contact_sale.id if len(contact_sale) == 1 else False,
            'type': 'ir.actions.act_window',
            'domain': domain
        }
