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
        copy=False,
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

    _sql_constraints = [
        ('revision_unique',
         'unique(unrevisioned_name, revision_number, company_id)',
         'Order Reference and revision must be unique per Company.'),
    ]
    
    #_sql_constraints = [
     #   ('name_uniq',
      #  'unique(product_id)',
       # 'You can not create two quality check point for same Product !'),
    #]

    def new_revision(self):
        #self.ensure_one()
        old_name = self.name
        revno = self.revision_number
        self.write({'name': '%s-%02d' % (self.unrevisioned_name,
                                         revno + 1),
                    'revision_number': revno + 1})
        for i in self:          
            defaults = {'name': old_name,
                        'revision_number': revno + i.id,
                        'active': False,
                        #'state': 'cancel',
                        'current_revision_id': self.id,
                        'unrevisioned_name': self.unrevisioned_name,
                        }
        old_revision = super(QualityPoint, self).copy(default=defaults)
        #self.button_draft()
        msg = _('New revision created: %s') % self.name
        self.message_post(body=msg)
        old_revision.message_post(body=msg)
        return True
    
    @api.model
    def create(self, vals):
        if 'revision_number' not in vals or vals['revision_number'] == '/':
            vals['revision_number'] = self.env['ir.sequence'].next_by_code('quality.point') or '/'
        return super(QualityPoint, self).create(vals)
    
    @api.model
    def create(self, values):
        if 'unrevisioned_name' not in values:
            if values.get('name', '/') == '/':
                seq = self.env['ir.sequence']
                values['name'] = seq.next_by_code('quality.point') or '/'
            values['unrevisioned_name'] = values['name']
        return super(QualityPoint, self).create(values)
