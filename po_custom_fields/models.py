# -*- coding: utf-8 -*-

from odoo import _, api, fields, models

class Purchase(models.Model):
    _inherit = "purchase.order"
    

    warranty = fields.Char('Warranty')
    warranty_term = fields.Selection([
        ('days', 'Days'),
        ('months', 'Months'),
        ('years', 'Years'),
        ], string='Warranty Term', default='days')
    delivery_schedule_id = fields.Many2one('delivery.schedule', string='Delivery Schedule')
    
    
class DeliverySchedule(models.Model):
    _name ='delivery.schedule'
    
    code = fields.Char('Code')
    name = fields.Char('Name')
