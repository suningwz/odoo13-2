# -*- coding: utf-8 -*-

from odoo import _, api, fields, models

class QualityCheckInherit(models.Model):
    _inherit = "quality.check"
    

    control_point = fields.Char(string='Control Point',readonly=True, compute='_compute_values', store= True)
    quality_point_type = fields.Char(string='Control Point Type',readonly=True, compute='_compute_values', store= True )
    norm = fields.Float(string='Control Point',readonly=True, compute='_compute_values', store= True)
    norm_unit = fields.Char(string='Control Point',readonly=True, compute='_compute_values', store= True)
    tolerance_min = fields.Float(string='Control Point',readonly=True, compute='_compute_values', store= True)
    tolerance_max = fields.Float(string='Control Point', compute='_compute_values', store= True)
    
    @api.depends('point_id')
    def _compute_values(self):
        
        self.control_point = self.point_id.name
        self.quality_point_type = self.point_id.test_type_id.name
        self.norm = self.point_id.norm
        self.norm_unit = self.point_id.norm_unit
        self.tolerance_min = self.point_id.tolerance_min
        self.tolerance_max = self.point_id.tolerance_max
        
        
    
    
    
    
    
    
    
    
