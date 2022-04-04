# -*- coding: utf-8 -*-
from odoo import http, _
from odoo.http import request


class Website(http.Controller):
    """Class where controllers are defined."""

    @http.route(['/contacts'], type='http', auth="public", website=True)
    def contacts(self, **data):
        """Function to get the records sets of res.partner.
        :return: record set"""
        contacts = request.env['res.partner'].search([])
        return request.render(
            "advance_action.contacts_list", {
                'contacts_list': contacts
            })

    @http.route(['/contacts/details/<model("res.partner"):contacts>'], type='http', auth='public', website=True)
    def contacts_detail(self, contacts):
        """Function to get details on the click of selected record.
        :return: record set"""
        return request.render("advance_action.contacts_detail", {'details': contacts})
