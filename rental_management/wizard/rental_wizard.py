"""This model is for Rental Management Wizard."""

from odoo import models, fields, api


class RentalManagementWizard(models.TransientModel):
    """This class is for Fields and Function for wizard."""
    _name = "rental.wizard"
    _description = "Rental Management Wizard"

    type_name = fields.Char(string="Name")
    code = fields.Char(string="Code")
    description = fields.Text(string="Description")

    def create_wizard(self):
        """Function to Create new record from wizard."""
        res = self.env['rental.type'].create({
            'type_name': self.type_name,
            'code': self.code,
            'description': self.description
        })
        print("====================>", res)

    def write_wizard(self):
        """Function to Update record from wizard."""
        context = self._context
        rental_type = self.env[context["active_model"]].browse(context["active_id"])
        res = rental_type.write({
            'type_name': self.type_name,
            'code': self.code,
            'description': self.description
        })
        print("===================>", res)
