# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class JobCosting(models.Model):
    _inherit = 'job.costing'

    #@api.multi
    def _invocie_count(self):
#        invoice_obj = self.env['account.invoice']
        invoice_obj = self.env['account.move']
        for cost_sheet in self:
            cost_sheet.invoice_count = invoice_obj.search_count([('job_cost_id', '=',cost_sheet.id)])

    invoice_ids = fields.One2many(
#        'account.invoice',
        'account.move',
        'job_cost_id',
        store=True,
    )
    invoice_count = fields.Integer(
        compute="_invocie_count"
    )
    billable_method = fields.Selection(
        string='Customer Invoice Billable Method',
        selection=[('based_on_apq','Based On Actual Purchase Qty'),
                   ('based_on_avbq','Based On Actual Vendor Bill Qty'),
                   ('based_on_mi','Based On Manual Invoice')],
        required=True,
        default='based_on_avbq'
    )

    #@api.multi
    def action_view_invoice(self):
        invoice_lst = []
        for invoice in self.invoice_ids:
            invoice_lst.append(invoice.id)
#        action = self.env.ref('account.action_invoice_tree1')
        action = self.env.ref("account.action_move_out_invoice_type")
        action = action.read()[0]
        action['domain'] = "[('id','in',[" + ','.join(map(str, invoice_lst)) + "])]"
        
        return action
