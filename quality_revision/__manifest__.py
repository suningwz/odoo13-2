# -*- coding: utf-8 -*-
{
    "name" : "Quality Revision",
    "category": "Quality",
    "summary": " ",
    "description": """ """,
    "version":"13.0.2",
    "depends" : ["base","purchase", "quality","quality_control"],
    "application" : True,
    "data": [
        'views/quality_views.xml',
        'views/quality_check_views.xml',
    ],
    #"images": ["static/description/background.png", ],
    "post_init_hook": "post_init_hook",
    "installable" : True,
   
}
