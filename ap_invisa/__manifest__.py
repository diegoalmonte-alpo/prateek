# -*- coding: utf-8 -*-
#################################################################################
# Author      : Alpo Multimedia Services. (<https://alpo.com.do/>)
# Copyright(c): 2021-Present Alpo Multimedia Services, SRL.
# All Rights Reserved.
#
#
#
# This program is copyright property of the author mentioned above.
# You can`t redistribute it and/or modify it.
#
#
#################################################################################
{
    # Module information
    "name": "Invisa",
    "summary": "Modificaciones para Super Techos",
    "version": "13.0.1.0.0",
    "category": "Sales",
    "website": "https://alpo.com.do",
    "author": "Alpo Multimedia",
    "license": "LGPL-3",
    # Dependencies
    "depends": ["sale_management", "sale_timesheet", "account", "stock",'stock_landed_costs'],
    # Views
    "data": ["security/ir.model.access.csv",
             "views/sale_product_view.xml",
             "views/report_saleorder.xml",
             "views/account_move.xml",
             "views/account_payment.xml",
             "views/product_template.xml",
             "views/product_views.xml",
             "views/stock_picking.xml",
             "views/stock_landed_cost.xml",
             "reports/report_deliveryslip.xml",
             "reports/report_purchase_order.xml",
             ],
    # Techical
    "images"               :  ['static/description/Banner.jpg'],
    "application"          :  True,
    "installable"          :  True,
}
