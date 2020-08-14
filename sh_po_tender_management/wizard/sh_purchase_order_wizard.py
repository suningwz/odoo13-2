# -*- coding: utf-8 -*-


from odoo import models,fields,api,_

class ShPurchaseOrderWizard(models.TransientModel):
    _name='purchase.order.wizard'
    _description='Purchase Order Wizard'
    
    sh_group_by_partner = fields.Boolean("Group By")
    
    def action_create_po(self):
        context = dict(self._context or {})
        purchase_order_line = self.env['purchase.order.line'].sudo().search([('id','in',context.get('active_ids'))])
        if purchase_order_line:
            if self.sh_group_by_partner==False:
                order_ids =[]
                for order_line in purchase_order_line:
                    purchase_order_id = self.env['purchase.order'].sudo().create({
                        'partner_id':order_line.partner_id.id,
                        'date_order':fields.Datetime.now(),
                        'agreement_id':order_line.agreement_id.id,
                        'user_id':self.env.user.id,
                        'date_planned':order_line.date_planned,
                        'selected_order':True,
                        })
                    order_ids.append(purchase_order_id.id)
                    line_vals={
                        'order_id':purchase_order_id.id,
                        'product_id':order_line.product_id.id,
                        'name':order_line.product_id.name,
                        'date_planned':order_line.date_planned,
                        'status':'draft',
                        'product_uom':order_line.product_id.uom_id.id,
                        'product_qty':order_line.product_qty,
                        'price_unit':order_line.price_unit,
                        'taxes_id':[(6,0,order_line.taxes_id.ids)]
                        }
                    purchase_order_line = self.env['purchase.order.line'].sudo().create(line_vals)
                return {
                'name': _("Purchase Orders/RFQ's"),
                'type': 'ir.actions.act_window',
                'res_model': 'purchase.order',
                'view_type':'form',
                'view_mode': 'tree,form',
                'domain':[('id','in',order_ids),('selected_order','=',True)],
                'target':'current'
                    }
            else:
                partner_list = []
                agreement_id = None
                order_ids =[]
                for order_line in purchase_order_line:
                    if order_line.partner_id and order_line.partner_id not in partner_list:
                        partner_list.append(order_line.partner_id)
                    agreement_id = order_line.agreement_id.id
                for partner in partner_list:
                    order_vals = {}
                    order_vals = {
                            'partner_id':partner.id,
                            'user_id':self.env.user.id,
                            'date_order':fields.Datetime.now(),
                            'agreement_id':agreement_id,
                            'selected_order':True,
                            }
                    order_id = self.env['purchase.order'].create(order_vals)
                    order_ids.append(order_id.id)
                    line_ids = []
                    for order_line in purchase_order_line:
                        if order_line.partner_id.id == partner.id:
                            order_line_vals={
                            'order_id':order_id.id,
                            'product_id':order_line.product_id.id,
                            'name':order_line.product_id.name,
                            'date_planned':order_line.date_planned,
                            'status':'draft',
                            'product_uom':order_line.product_id.uom_id.id,
                            'product_qty':order_line.product_qty,
                            'price_unit':order_line.price_unit,
                            'taxes_id':[(6,0,order_line.taxes_id.ids)]
                            }
                            line_ids.append((0,0,order_line_vals))
                    order_id.order_line = line_ids
                return {
                'name': _("Purchase Orders/RFQ's"),
                'type': 'ir.actions.act_window',
                'res_model': 'purchase.order',
                'view_type':'form',
                'view_mode': 'tree,form',
                'domain':[('id','in',order_ids),('selected_order','=',True)],
                'target':'current'
                    }
                
