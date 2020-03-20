# -*- coding: utf-8 -*-

{
    'name': 'Gate Entry',
    'summary': """Generating Gate entry slip in delivery orders and receipts""",
    'version': '13.0.1.0.0',
    'description': """Generating Gate entry slip in delivery orders and receipts""",
    'category': 'Inventory',
    'depends': ['base', 'stock'],
    'license': 'LGPL-3',
    'data': [
        'views/gate_in_views.xml',
        'views/gate_out_views.xml',
        'data/ir_sequence_indata.xml',
        'data/ir_sequence_outdata.xml',
        'report/gatein_pass_template.xml',
        'report/gateout_pass_template.xml',
        'report/gate_pass_report.xml',
    ],
    'demo': [],
    #'images': ['static/description/banner.png'],
    'installable': True,
    'auto_install': False,
    'application':True,
}
