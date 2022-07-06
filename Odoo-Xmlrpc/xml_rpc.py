url = 'http://localhost:15000/'
db = 'flow_db'
username = 'admin'
password = 'admin'

import xmlrpc.client
import csv
from datetime import datetime
import os

common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
version = common.version()
print("------------details", version)

uid = common.authenticate(db, username, password, {})
print("============UID", uid)

models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))

with open('/home/odoo/Downloads/res_partner.csv', newline='') as csv_file:
    csv_file = csv.DictReader(csv_file)
    excel_row = 2
    print(">>>>>>>>>>>>>>>>>>>>>>>>Excel Data", csv_file)
    partner_count = models.execute_kw(db, uid, password, 'res.partner', 'search_count', [[]])
    print("========================Partner Count", partner_count)

    for row in csv_file:
        rec = dict(row)
        print("----------------rec", rec)
        if excel_row >= 2:
            partner_tmpl_id = models.execute_kw(db, uid, password, 'res.partner', 'search',
                                                [[['email', '=', rec['email']]]])
            company_data = models.execute_kw(db, uid, password, 'res.company', 'search',
                                             [[['name', '=', rec['company_id']]]])
        if rec['company_id']:
            if not company_data:
                company_data = models.execute_kw(db, uid, password, 'res.company', 'create',
                                                 [[{'name': rec['company_id'],
                                                    'partner_id': 3}]])
                print("--------------company", company_data)
            country_data = models.execute_kw(db, uid, password, 'res.country', 'search',
                                             [[['name', '=', rec['country_id']]]])
            print("::::::::::::::::::Company", company_data)
            print("::::::::::::::::::Country", country_data)
            print("::::::::::::::::::", partner_tmpl_id)
            vals = {'name': rec['name'],
                    'city': rec['city'],
                    'phone': rec['phone'],
                    'company_id': company_data[0],
                    'country_id': country_data[0]}
            # if country_data:
            #     vals['country_id'] = rec['country_id']
            print("----------------vals", vals)
            if not partner_tmpl_id:
                partner_tmpl_id = models.execute_kw(db, uid, password, 'res.partner', 'create', [vals])
            else:
                partner_tmpl_id = models.execute_kw(db, uid, password, 'res.partner', 'write',
                                                    [[partner_tmpl_id[0]], vals])

    partner_data_company = models.execute_kw(db, uid, password, 'res.partner', 'search', [
        [['parent_id', '=', 'My Company(San Francisco)']]])
    print("````````````Partner", partner_data_company)
    country_data = models.execute_kw(db, uid, password, 'res.country', 'search', [
        [['name', '=', 'United States']]])
    print("~~~~~~~~~~~~~Country", country_data)
    edit_data = models.execute_kw(db, uid, password, 'res.partner', 'write',
                                  [partner_data_company, {'country_id': country_data}])
    print("------------Partner Edit", edit_data)
    city_data = models.execute_kw(db, uid, password, 'res.partner', 'search', [[['city', '=', 'Berlin']]])
    print("------------City", city_data)
    delete_data = models.execute_kw(db, uid, password, 'res.partner', 'unlink', [city_data])
    print("------------Delete", delete_data)
    partner_data = models.execute_kw(db, uid, password, 'res.partner', 'search_count', [[]])
    print("--------------Data Count", partner_data)
