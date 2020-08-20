# -*- coding: utf-8 -*-
{
    "name" : "Custom PO Report",
    "category": "Report",
    "summary": " ",
    "description": """ """,
    "version":"13.0.2",
    "depends" : ["base","purchase", "quality","quality_control","purchase_stock",],
    "application" : False,
    "data": [
        'report_views.xml',
        'report_purchaseorder.xml',
        'views.xml',
    ],
    
    "installable" : True,
   
}
