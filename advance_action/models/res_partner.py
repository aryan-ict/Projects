"""This model is for Advance Action."""

from odoo import models, fields, api


class ResPartner(models.Model):
    """This class is for create and write fucntion"""
    _inherit = 'res.partner'

    def update_rec(self):
        """Function to Update record."""
        self.write({'name': "Edward Newton",
                    'phone': 1523647891,
                    'email': 'xyz@gmail.com0'})

    def create_rec(self):
        self.create({'name': "Newt Schamander",
                     'phone': 9876543215,
                     'email': 'hogwarts@gmail.com0'})
