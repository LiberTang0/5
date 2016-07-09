# -*- coding: utf-8 -*-
# Part of eCore. See LICENSE file for full copyright and licensing details.

{
    'name' : 'Analytic Accounting',
    'version': '1.1',
    'website' : 'http://www.ecore.cool/page/accounting',
    'category': 'Hidden/Dependency',
    'depends' : ['base', 'decimal_precision', 'mail', 'report'],
    'description': """
Module for defining analytic accounting object.
===============================================

In eCore, analytic accounts are linked to general accounts but are treated
totally independently. So, you can enter various different analytic operations
that have no counterpart in the general financial accounts.
    """,
    'data': [
        'security/analytic_security.xml',
        'security/ir.model.access.csv',
        'views/analytic_view.xml',
        'wizard/account_analytic_chart_view.xml',
    ],
    'demo': [
        'data/analytic_demo.xml',
        'data/analytic_account_demo.xml',
    ],
    'installable': True,
    'auto_install': False,
}