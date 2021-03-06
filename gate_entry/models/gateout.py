# -*- coding: utf-8 -*-


from odoo import api, fields, models, tools,_
from datetime import datetime, timedelta


class GateEntryOut(models.Model):
    _name = "gate.out"
    _description = 'Gate Out Entry'
    
    user_id = fields.Many2one("res.users","Security Name",default=lambda self: self.env.user)
    name = fields.Char("Sequence Number", required=True, copy=False, index=True,default =lambda self: _('New'))
    date = fields.Datetime("Entry Date")
    partner_id = fields.Many2one("res.partner", "Customer Name")
    partner_phone = fields.Char("Customer Contact Number", related='partner_id.phone')
    partner_email = fields.Char("Customer Email", related='partner_id.email')
    stock_picking_id = fields.Many2one("stock.picking","Dispatch No")
    stock_picking_date = fields.Datetime("Dispatch Date")
    #stock_move_id = fields.
    stock_picking_line_ids = fields.One2many(
        "stock.move.inherit.out", "gate_out_id", "Item Description")
    origin = fields.Char("Source Doc")
    vehicle_no = fields.Char(string='Vehicle Number')
    vehicle_driver_name = fields.Char(string='Driver Name')
    driver_contact_number = fields.Char(string='Driver Contact No')
    #corresponding_company = fields.Char(string='Company')
    
    location_type_id = fields.Many2one('stock.picking.type',"Operational type-Warehouse")
    location_id = fields.Many2one(
        'stock.location', "Source Location")
    notes = fields.Text('Notes')
    
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirm', 'Confirmed'),
        ], string='Status', readonly=True, copy=False, index=True, default='draft')
    
    ## confirm button
    def action_confirm(self):
        res = self.env['stock.picking'].search([('name', '=' , self.stock_picking_id.name)])
        res.write({'gateout_entry_id': self.id})
        return self.write({'state': 'confirm'})
    
    ## Auto sequence
    
    @api.model
    def create (self,vals):
        if vals:
            vals['name'] = self.env['ir.sequence'].next_by_code('gate.out') or _('New')
        return super(GateEntryOut,self).create(vals)
        
    ##Onchange for stock.picking date in gate in form based on stock picking scheduled date
    
    @api.onchange('stock_picking_id')
    def on_change_select(self):
        values = {
            'stock_picking_date': self.stock_picking_id.scheduled_date or False, 
            'partner_id': self.stock_picking_id.partner_id and self.stock_picking_id.partner_id.id or False, 
            'origin': self.stock_picking_id.origin or False,
        }
        self.update(values)
        
    ##Get lines items from stock.picking to gate in form
    @api.onchange('stock_picking_id')
    def on_change_picking(self):
        res = self.env['stock.picking']
        val = res.move_ids_without_package.search([('picking_id', '=' , self.stock_picking_id.name)])
        print(val.picking_id.name)
        r = [(5, 0, 0)]
        value = {}
        
        if self.stock_picking_id:
            for line in val:
                data = { 'product_id':line.product_id.id,
                         'product_qty':line.product_uom_qty,
                         'product_done_qty':line.quantity_done,
                         'product_uom':line.product_uom.name,
                       }
                print(data)
                r.append((0,0,data))
            value.update(stock_picking_line_ids = r)
            return {'value': value} 
    
    
class StockPickingInherit(models.Model):
    _name = 'stock.move.inherit.out'
    
    gate_out_id = fields.Many2one("gate.out", "Gate Out Entries")
    product_id = fields.Many2one(
        'product.product', 'Product', index=True, required=True) 
    product_qty = fields.Float(
        'Quantity',default=0.0, required=True)
    product_done_qty = fields.Float(
        'Done Quantity',default=0.0, required=True)
    product_uom = fields.Char(
        'UoM')
        
class GatePassStockInherit(models.Model):
    _inherit = 'stock.picking'

    gateout_entry_id = fields.Many2one("gate.out", "Gate Out Entry",copy=False, index=True)
