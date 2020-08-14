# -*- coding: utf-8 -*-


from odoo import models, fields


class ResPartner(models.Model):
    _inherit = 'res.users'

    is_tendor_vendor = fields.Boolean('Is Tender Portal User')
