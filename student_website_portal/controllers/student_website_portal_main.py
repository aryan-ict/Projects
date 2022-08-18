from odoo import http, _
from odoo.http import request
import json
from odoo.addons.portal.controllers import portal


class Website(http.Controller):

    @http.route('/my/students', type='http', auth='user', website=True)
    def student(self):
        student_list = request.env['student.website.portal'].search([('allocated_id', '=', request.env.uid)])
        print("-----------------Student List", student_list)
        return request.render('student_website_portal.student_list_page', {
            'student_list': student_list
        })

    @http.route(['/my/students/details/<model("student.website.portal"):student>'], type='http', auth='user', website=True)
    def student_detail(self, student):
        print("----------------Students", student)
        return request.render("student_website_portal.student_portal_content", {
            'detailed_content': student
        })

    @http.route('/my/student/create', type='http', auth='user', website=True)
    def create_student(self, **args):
        print("-------------Edit", args)
        state_ids = request.env['res.country.state'].search([])
        country_ids = request.env['res.country'].search([])
        teacher_ids = request.env['res.users'].search([])
        return request.render("student_website_portal.student_create_form", {
            'state_id': state_ids,
            'country_id': country_ids,
            'teacher_id': teacher_ids
        })

    @http.route('/thankyou', type='json', auth='user')
    def thankyou(self, **args):
        print("----------------Args", args)
        country = args.get('country_id')
        print("----------------Args", country)
        state_ids = request.env['res.country.state'].search([('country_id', '=', int(country))])
        print("--------------State", state_ids)
        if args:
            request.env['student.website.portal'].create({
                'name': args.get('name'),
                'phone': args.get('phone'),
                'birth_date': args.get('birth_date'),
                'email': args.get('email'),
                'allocated_id': args.get('allocated_id'),
                'street': args.get('street'),
                'street2': args.get('street2'),
                'city': args.get('city'),
                'zip': args.get('zip'),
                'country': args.get('country_id'),
            })
        return state_ids


class StudentCustomerPortal(portal.CustomerPortal):

    def _prepare_home_portal_values(self, counters):
        print("------------Counters", counters)
        vals = super(StudentCustomerPortal, self)._prepare_home_portal_values(counters)
        student_count = request.env['student.website.portal'].search_count([('allocated_id', '=', request.env.uid)])
        vals.update({
            'student_count': student_count
        })
        return vals
