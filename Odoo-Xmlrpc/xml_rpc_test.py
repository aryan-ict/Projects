url = 'http://localhost:15000/'
db = 'batch_sale_workflow_db'
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
partner_data_company = models.execute_kw(db, uid, password, 'res.partner', 'search', [
    [['parent_id', '=', 'my company(san francisco)']]])
print("````````````Partner", partner_data_company)
country_data = models.execute_kw(db, uid, password, 'res.country', 'search', [
    [['name', '=', 'United States']]])
print("~~~~~~~~~~~~~Country", country_data)
edit_data = models.execute_kw(db, uid, password, 'res.partner', 'write', [partner_data_company, {'country_id': 233}])
print("------------Partner Edit", edit_data)
city_data = models.execute_kw(db, uid, password, 'res.partner', 'search', [[['city', '=', 'Berlin']]])
print("------------City", city_data)
delete_data = models.execute_kw(db, uid, password, 'res.partner', 'unlink', [city_data])
print("------------Delete", delete_data)
partner_data = models.execute_kw(db, uid, password, 'res.partner', 'search_count', [[]])
print("--------------Data Count", partner_data)

