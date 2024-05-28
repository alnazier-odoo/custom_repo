# -*- coding: utf-8 -*-

{
    'name': 'Auctions',
    'version': '16.0.1.1.0',
    'sequence': -100,
    'summary': """
                   Financial Control 
                     """,
    'author': 'Mohamed Esam',
    'website': '',
    'depends': ['mail', 'base'],
    'data': ['views/auctions_view.xml',
             'views/buyer_database.xml',
             'views/buyer_buyer.xml',
             'views/sales_focal_point.xml',
             'views/technical_focal_point.xml',
             'views/auction_stages.xml',
             'views/buyer_stage.xml',
             'views/visits_stages.xml',
             'views/visits_status.xml',
             'views/site_visits.xml',
             'security/ir.model.access.csv'],

    'installable': True,
    'auto_install': False,
    'application': True,
    'license': 'AGPL-3',

}
