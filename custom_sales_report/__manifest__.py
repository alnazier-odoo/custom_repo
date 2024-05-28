# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Custom Sales Report',
    'version': '16.0.0',
    'summary': 'Print Sales Reports',
    'sequence': -100,
    'description': """Print reports for sales operations by the date, salepersons, and customers""",
    'category': '',
    'depends': [
        'sale',
        'base'
    ],
    'data': [
        'security/ir.model.access.csv',
        'wizards/sales_report_wizard_view.xml',
        'views/sale_order_view.xml',
        'reports/report_sales_action_wizard_temp.xml',

    ],
    'demo': [],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',

}
