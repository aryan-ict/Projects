from odoo import http, _
from odoo.http import request
import base64


class Website(http.Controller):

    @http.route('/contact_form', type='http', auth='user', website=True)
    def contact_form(self, **kw):
        """Function for /contact_form controller where contact form is rendered."""
        return request.render('aryanmodh_02062022.contact_form', {})

    @http.route('/contact_form/thank_you', type='http', auth='user', website=True)
    def create_form(self, **kw):
        """Function for /contact_form/thank_you controller
        where data is being created in backend."""
        print("++++++++++++++++++++", kw)
        attached_files = request.httprequest.files.getlist('image_1920')
        for file in attached_files:
            print("--------------------------file", file)
            partner = request.env['res.partner'].create({
                'name': kw.get('name'),
                'email': kw.get('email'),
                'phone': kw.get('phone'),
                'image_1920': base64.b64encode(file.read())
            })
            print("------------------partner", partner)
        return request.render('aryanmodh_02062022.contact_thank_you', {})
