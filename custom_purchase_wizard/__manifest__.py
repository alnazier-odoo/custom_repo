# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'custom purchase report wizards',
    'version': '16.0.0',
    'summary': 'Control Monitors',
    'sequence': 100,
    'description': """""",
    'category': '',
    'depends': ['purchase', 'base'

    ],
    'data': [
        'security/ir.model.access.csv',
        'wizards/purchase_report_wizard.xml',
        'views/purchase_order.xml',
        'reports/reports_action_wizards.xml',

    ],
    'demo': [],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
    'application': True,
    'autoinstall': False,
}
