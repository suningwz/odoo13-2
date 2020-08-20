# -*- coding: utf-8 -*-

from odoo import _, api, fields, models


class QualityPoint(models.Model):
    _inherit = "quality.point"

    current_revision_id = fields.Many2one(
        comodel_name='quality.point',
        string='Current revision',
        readonly=True,
    )
    old_revision_ids = fields.One2many(
        comodel_name='quality.point',
        inverse_name='current_revision_id',
        string='Old revisions',
        readonly=True,
        context={'active_test': False},
    )
    revision_number = fields.Integer(
        string='Revision',
        default = 1,
    )
    unrevisioned_name = fields.Char(
        string='Order Reference',
        copy=False,
        readonly=True,
    )
    active = fields.Boolean(
        string='Active',
        default=True,
    )

    
    
    #_sql_constraints = [
     #   ('name_uniq',
      #  'unique(product_id)',
       # 'You can not create two quality check point for same Product !'),
    #]

    
    def new_revision(self):
        for cur_rec in self:
            old_name = self.name
            self.write({'name': '%s-%02d' % (cur_rec.unrevisioned_name,
                                         cur_rec.revision_number ),
                    'revision_number': cur_rec.revision_number})
            
            #cur_rec.name = str(cur_rec.unrevisioned_name) +' - '+ str(cur_rec.revision_number)
            vals = {
                'name': old_name,
                'active': False,
                'revision_number': cur_rec.revision_number,
                'current_revision_id': cur_rec.id,
                'unrevisioned_name': self.unrevisioned_name,
            }
            cur_rec.copy(default=vals)
            cur_rec.state = 'draft'
#             so_copy.is_revision_quote = True
            cur_rec.revision_number += 1
    
    
    
    @api.model
    def create(self, values):
        if 'unrevisioned_name' not in values:
            if values.get('name', '/') == '/':
                seq = self.env['ir.sequence']
                values['name'] = seq.next_by_code('quality.point') or '/'
            values['unrevisioned_name'] = values['name']
        return super(QualityPoint, self).create(values)
