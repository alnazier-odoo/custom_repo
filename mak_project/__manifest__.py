# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Project Screen',
    'version': '16.0.0',
    'summary': 'Control Monitors',
    'sequence': -100,
    'description': """Project Manager Control""",
    'category': '',
    'depends': [
        'mail',
        'project',
        'base'
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/mom_view.xml',
        'views/action_item_view.xml',
        'views/action_tag_view.xml',
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
    'application': True,
    'autoinstall': False,
}
