# -*- coding: utf-8 -*-

from odoo import _, api, fields, models

class QualityPurchase(models.Model):
    _inherit = "purchase.order"
    

current_revision_id = fields.Many2one('quality.check',string='Current revision')
