# -*- coding: utf-8 -*-

from odoo import models, api

class PurchaseCUstomReport(models.AbstractModel):

    _name = 'report.po_custom_report.report_purchaseorder'
    
    
    @api.model
    def _get_report_values(self, docids, data=None):
        report_model = self.env['ir.actions.report']._get_report_from_name('po_custom_report.report_purchaseorder')
        obj = self.env["purchase.order"].browse(docids)
        quality_obj = self.env["quality.check"].search([('purchase_id', '=', obj.name)])
        order_lines = obj.order_line
        for i in quality_obj:
            print(i.name)
            rec = i
        
        
        #for i in order_lines:
         #   print(i)
          #  if i.product_id.id == quality_obj.product_id.id:
           #     print(quality_obj.name)
            #rec = quality_obj 
        return {
            'docs':obj,
            'doc_model':report_model.model,
            'quality': quality_obj, 
            }
