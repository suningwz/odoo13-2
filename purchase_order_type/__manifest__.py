# -*- coding: utf-8 -*-

{'name': 'Purchase Order Type',
 'version': '13.0.1.0.0',
 
 'license': 'AGPL-3',
 'category': 'Purchase Management',
 'depends': ['purchase',
             ],
 'website': 'http://www.camptocamp.com',
 'data': ['security/ir.model.access.csv',
          'views/view_purchase_order_type.xml',
          'views/view_purchase_order.xml',
          'views/res_partner_view.xml',
          'data/purchase_order_type.xml',
          ],
 'test': [],
 'installable': True,
 'auto_install': False,
 }
