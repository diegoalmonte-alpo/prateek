# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2015 DevIntelle Consulting Service Pvt.Ltd (<http://www.devintellecs.com>).
#
#    For Module Support : devintelle@gmail.com  or Skype : devintelle 
#
##############################################################################

{
    'name': 'Vendor Statement & Aging',
    'version': '13.0.1.0',
    'sequence':1,
    'category': 'Generic Modules/Accounting',
    'description': """
odoo Module will print vendor statement with Monthly aging 4

         partner Aging,
         customer Aging,
         odoo partner Aging
         odoo Vendor Aging,
         odoo partner statement ,
         odoo Vendor statement,
         odoo Vendor statement by invoice date,
         odoo Vendor statement by due date,
         Vendor statement by due date,
         Vendor statement by invoice date,
         partner statement by due date,
         partner statement by invoice date,
         outstanding statement,
         Vendor outstanding statement,
         Odoo Vendor outstanding statement,
         odoo Vendor overdue payment,
         Vendor overdue payment, 
         Odoo overdue payment, 
         Odoo overdue statement,
Vendor Statement & Aging
Odoo Vendor Statement & Aging
Vendor statement 
Odoo vendor statement 
Manage vendor statement
Odoo manage vendor statement
Manage vendor aging 
Odoo manage vendor aging 
odoo app will print vednor statement with detailed view of invoices,payments by invoice & due date and print partner again by month in same vendor statement.
Print Vendor Account Statement 
Odoo Print Vendor Account Statement 
Ageing by due Date and invoice Date
Odoo Ageing by due Date and invoice Date
Vendor account statement 
Odoo vendor account statement 
Manage vendor account 
Odoo manage vendor account 
Vendor statement aging 
Odoo vendor statement aging 


    """,
    'summary':'Odoo app Print vendor Statement with invoice date/due date and partner aging, Vendor statement, vendor account statement, Vendor overdue payment, Vendor outstanding statement, Vendor statement by invoice date, a statement by the due date, partner Aging, customer Aging',
    'depends': ['sale_management','purchase'],
    'data': [
        'wizard/vendor_statement_views.xml',
        'report/header.xml',
        'report/vendor_statement_template.xml',
        'report/report_menu.xml',
        'edi/mail_template.xml',
    ],
    'demo': [],
    'test': [],
    'css': [],
    'qweb': [],
    'js': [],
    'images': ['images/main_screenshot.png'],
    'installable': True,
    'application': True,
    'auto_install': False,
    
    #author and support Details
    'author': 'DevIntelle Consulting Service Pvt.Ltd',
    'website': 'http://www.devintellecs.com',    
    'maintainer': 'DevIntelle Consulting Service Pvt.Ltd', 
    'support': 'devintelle@gmail.com',
    'price':29.0,
    'currency':'EUR',
    #'live_test_url':'https://youtu.be/A5kEBboAh_k',
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
