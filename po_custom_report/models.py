# -*- coding: utf-8 -*-

from odoo import _, api, fields, models

class QualityPurchase(models.Model):
    _inherit = "quality.check"
    

    purchase_id = fields.Many2one('purchase.order',string='Purchase Order',related = 'picking_id.purchase_id')
