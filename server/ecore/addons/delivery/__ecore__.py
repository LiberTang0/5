# -*- coding: utf-8 -*-
# Part of eCore. See LICENSE file for full copyright and licensing details.


{
    'name': 'Delivery Costs',
    'version': '1.0',
    'category': 'Sales Management',
    'description': """
Allows you to add delivery methods in sale orders and picking.
==============================================================

You can define your own carrier for prices. When creating
invoices from picking, the system is able to add and compute the shipping line.
""",
    'depends': ['sale_stock'],
    'data': [
        'security/ir.model.access.csv',
        'views/delivery_view.xml',
        'views/partner_view.xml',
        'data/delivery_data.xml',
        'views/report_shipping.xml',
        'views/report_deliveryslip.xml'

    ],
    'demo': ['data/delivery_demo.xml'],
    'test': [
        '../account/test/account_minimal_test.xml',
    ],
    'installable': True,
}
