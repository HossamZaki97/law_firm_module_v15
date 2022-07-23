# -*- coding: utf-8 -*-

from odoo import models,fields, api, _
from odoo.exceptions import ValidationError, UserError

class JobcostInvoice(models.TransientModel):
    _name = 'jobcost.invoice'
    _description = 'jobcost.invoice'

    partner_id = fields.Many2one(
        'res.partner',
        required = True,
        string='Customer',
    )
    invoice_date = fields.Date(
        'Invoice Date',
        default=fields.date.today(),
        required=True,
    )
    material_invoice = fields.Boolean(
        'Include Material Lines',
    )
    labour_invoice = fields.Boolean(
        'Include Labour Lines',
    )
    overhead_invoice = fields.Boolean(
        'Include Overhead Lines',
    )
    
    @api.model
    def default_get(self, fields):
        rec = super(JobcostInvoice, self).default_get(fields)
        active_id = self.env['job.costing'].browse(self._context.get('active_id'))
        partner = active_id.partner_id
        rec.update({
                'partner_id' : partner.id,
        })
        return rec
    
    #@api.multi
    def create_jobcost_invoice(self):
        active_id = self._context.get('active_id')
        job_costing = self.env['job.costing'].browse(active_id)
#        invoice_obj = self.env['account.invoice']
#        invoice_line_obj = self.env['account.invoice.line']
        invoice_obj = self.env['account.move']
        invoice_line_obj = self.env['account.move.line']
        invoice_list = []
        for invoices in job_costing.invoice_ids:
            invoice_list.append(invoices.id)
        for rec in self:
            invoice_ids = []
            partner_id = rec.partner_id
            invoice_name = job_costing.name
            currency_id = job_costing.currency_id
            material_line_ids = []
            inv_line_vals_lst = []
            if rec.labour_invoice != True and rec.material_invoice != True and rec.overhead_invoice!=True:
                raise ValidationError('Invoice not Created.')
            if rec.material_invoice:
                material_ids = job_costing.job_cost_line_ids
                for material_id in material_ids:
                    invoice_lst = []
                    
                    
                    
                    if job_costing.billable_method == 'based_on_avbq':
                        quantity = material_id.actual_invoice_quantity - material_id.invoice_qty
                    elif job_costing.billable_method == 'based_on_apq':
                        quantity = material_id.actual_quantity - material_id.invoice_qty
                    else:
                        quantity = material_id.manual_invoice_qty

                    if material_id.billable == 'billable' and quantity > 0.0:
                        for invoice_line_id in material_id.invoice_line_ids:
                            invoice_lst.append(invoice_line_id.id)

                        account_id = False
                        if material_id.product_id.id:
                            account_id = material_id.product_id.property_account_income_id.id or material_id.product_id.categ_id.property_account_income_categ_id.id
#                        if not account_id:
#                            inc_acc = ir_property_obj.get('property_account_income_categ_id', 'product.category')
#                            account_id = order.fiscal_position_id.map_account(inc_acc).id if inc_acc else False
                        if not account_id:
                            raise UserError(
                                _('There is no income account defined for this product: "%s". You may have to install a chart of account from Accounting app, settings menu.') % (material_id.product_id.name,))
                                
                        product_id = material_id.product_id
                        name = material_id.description
                        amount = material_id.sale_price
#                        quantity = material_id.actual_invoice_quantity - material_id.invoice_qty
                        uom_id = material_id.uom_id
                        
                        material_vals_line = {
                            'name': name,
                            'account_id': account_id,
                            'price_unit': amount,
                            'quantity': quantity,
#                            'uom_id': uom_id.id,
                            'product_uom_id': uom_id.id,
                            'product_id': product_id.id,
                            'job_cost_line_ids': [(4, material_id.id)],
                        }
                        inv_line_vals_lst.append((0, 0, material_vals_line))
#                        material_line_id = invoice_line_obj.create(material_vals_line)
#                        material_line_ids.append(material_line_id.id)
                        material_line_ids.append(material_vals_line)
#                        invoice_lst.append(material_line_id.id)
#                        material_id.invoice_line_ids = [(6, 0, invoice_lst)]
                        
                if not material_line_ids:
                    raise ValidationError('No Material lines found to create invoice.')
                
            if rec.labour_invoice:
                labour_ids = job_costing.job_labour_line_ids
                labour_line_ids = []
                for labour_id in labour_ids:
                    labour_invoice_lst = []
                    
                    
                    if job_costing.billable_method == 'based_on_avbq':
                        qty = labour_id.actual_hour - labour_id.invoice_hours
                    elif job_costing.billable_method == 'based_on_apq':
                        qty = labour_id.actual_hour - labour_id.invoice_hours
                    else:
                        qty = labour_id.manual_invoice_hours 
                    
                    
                    if labour_id.billable == 'billable' and qty > 0.0:
                        for invoice_line_id in labour_id.invoice_line_ids:
                            labour_invoice_lst.append(invoice_line_id.id)
                        
                        labour_account_id = False
                        if labour_id.product_id.id:
                            labour_account_id = labour_id.product_id.property_account_income_id.id or labour_id.product_id.categ_id.property_account_income_categ_id.id
                        
                        if not labour_account_id:
                            raise UserError(
                                _('There is no income account defined for this product: "%s". You may have to install a chart of account from Accounting app, settings menu.') % (labour_id.product_id.name,))
                        
                        product_id = labour_id.product_id
                        name = labour_id.description
                        amount = labour_id.sale_price
#                        qty = labour_id.actual_hour - labour_id.invoice_hours
                        uom_id = labour_id.uom_id
                        labour_vals_line = {
                            'name': name,
                            'account_id': labour_account_id,
                            'price_unit': amount,
                            'quantity': qty,
#                            'uom_id': uom_id.id,
                            'product_uom_id': uom_id.id,
                            'product_id': product_id.id,
                            'job_cost_line_ids': [(4, labour_id.id)],
                        }
                        inv_line_vals_lst.append((0, 0, labour_vals_line))
#                        labour_line_id = invoice_line_obj.create(labour_vals_line)
#                        labour_line_ids.append(labour_line_id.id)
#                        material_line_ids.append(labour_line_id.id)
                        labour_line_ids.append(labour_vals_line)
#                        labour_invoice_lst.append(labour_line_id.id)
#                        labour_id.invoice_line_ids = [(6, 0, labour_invoice_lst)] 
                        
                if not labour_line_ids:
                    raise ValidationError('No Labour lines found to create invoice.')
                    
            if rec.overhead_invoice:
                overhead_ids = job_costing.job_overhead_line_ids
                overhead_line_ids = []
                for overhead_id in overhead_ids:
                    overhead_invoice_lst = []
                    
                    
                    
                    if job_costing.billable_method == 'based_on_avbq':
                        qty = overhead_id.actual_invoice_quantity - overhead_id.invoice_qty
                    elif job_costing.billable_method == 'based_on_apq':
                        qty = overhead_id.actual_quantity - overhead_id.invoice_qty
                    else:
                        qty = overhead_id.manual_invoice_qty
                    
                    
                    
                    
                    if overhead_id.billable == 'billable' and qty > 0.0:
                        for invoice_line_id in overhead_id.invoice_line_ids:
                            overhead_invoice_lst.append(invoice_line_id.id)
                            
                        overhead_account_id = False
                        if overhead_id.product_id.id:
                            overhead_account_id = overhead_id.product_id.property_account_income_id.id or overhead_id.product_id.categ_id.property_account_income_categ_id.id
                        
                        if not overhead_account_id:
                            raise UserError(
                                _('There is no income account defined for this product: "%s". You may have to install a chart of account from Accounting app, settings menu.') % (overhead_id.product_id.name,))
                            
                        product_id = overhead_id.product_id
                        name = overhead_id.description
                        amount = overhead_id.sale_price#cost_price
                        uom_id = overhead_id.uom_id
                        
                        overhead_vals_line = {
                            'name': name,
                            'account_id': overhead_account_id,
                            'price_unit': amount,
                            'quantity': qty,
#                            'uom_id': uom_id.id,
                            'product_uom_id': uom_id.id,
                            'product_id': product_id.id,
                            'job_cost_line_ids': [(4, overhead_id.id)],
                        }
                        inv_line_vals_lst.append((0, 0, overhead_vals_line))
#                        overhead_line_id = invoice_line_obj.create(overhead_vals_line)
#                        overhead_line_ids.append(overhead_line_id.id)
#                        material_line_ids.append(overhead_line_id.id)
                        overhead_line_ids.append(overhead_vals_line)
#                        overhead_invoice_lst.append(overhead_line_id.id)
#                        overhead_id.invoice_line_ids = [(6, 0, overhead_invoice_lst)]
                        
                if not overhead_line_ids:
                    raise ValidationError('No Overhead lines found to create invoice.')

            material_vals = {
#                    'account_id': job_costing.partner_id.property_account_receivable_id.id,
                    'partner_id': partner_id.id,
#                    'invoice_line_ids': [(6, 0, material_line_ids)],
                    'invoice_line_ids': inv_line_vals_lst,
                    'currency_id': currency_id.id,
                    'job_cost_id': job_costing.id,
#                    'date_invoice': rec.invoice_date,
                    'invoice_date': rec.invoice_date,
#                    'type': 'out_invoice',
                    'move_type': 'out_invoice',
            }
            invoice_id = invoice_obj.create(material_vals)
            invoice_ids.append(invoice_id.id)
            invoice_list.append(invoice_id.id)
                
#            job_costing.invoice_ids = [(6, 0, invoice_list)]
#            action = self.env.ref('account.action_invoice_tree1')
            action = self.env.ref("account.action_move_out_invoice_type")
            action = action.read()[0]
            action['domain'] = "[('id','in',[" + ','.join(map(str, invoice_ids)) + "])]"
            return action
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
