# -*- coding: utf-8 -*-

from odoo import models, fields, api


class JonCostLine(models.Model):
    _inherit = 'job.cost.line'

    @api.model
    def _default_billable(self):
        rec = self._context.get('default_job_type')
        if rec == 'overhead':
            billable = 'not_billable'
        else:
            billable = 'billable'
        return billable

    #@api.multi
    def _compute_invoice_qty(self):
        for rec in self:
            rec.invoice_qty = 0.0
            if rec.job_type_id.job_type != 'labour':
#                rec.invoice_qty = 0.0
                qty = 0.0
#                print "-----------------------",rec
                for line in rec.invoice_line_ids:
#                    print "====================",line
                    qty += line.quantity
                    rec.invoice_qty = qty
    #@api.multi
    def _compute_invoice_hour(self):
        for rec in self:
            rec.invoice_hours = 0.0
            if rec.job_type_id.job_type == 'labour':
#                rec.invoice_hours = 0.0
                hour = 0.0
                for line in rec.invoice_line_ids:
                    hour += line.quantity
                    rec.invoice_hours = hour

    @api.onchange('product_id')
    def _onchange_product_id(self):
        result = super(JonCostLine, self)._onchange_product_id()
        for rec in self:
            rec.sale_price = rec.product_id.lst_price
        return result 

    billable = fields.Selection(
        selection=[('billable','Billable'),
         ('not_billable','Not Billable'),
        ],
        string="Is Billable",
        default=_default_billable,
    )
#    invoice_line_ids = fields.Many2many(
##        'account.invoice.line'
#        'account.move.line'
#    )
    invoice_line_ids = fields.Many2many(
        'account.move.line',
        'job_cost_line_invoice_rel',
        'job_cost_line_id',
        'invoice_line_id',
        string='Customer Invoice Lines',
        copy=False
    )
    invoice_qty = fields.Float(
        'Customer Invoiced Qty',
        compute="_compute_invoice_qty",
    )
    invoice_hours = fields.Float(
        'Invoiced Hour',
        compute="_compute_invoice_hour",
    )
    manual_invoice_qty = fields.Float(
        'Manual Invoiced Qty',
    )
    manual_invoice_hours = fields.Float(
        'Manual Invoiced Hour',
    )
    sale_price = fields.Float(
        string='Sale Price / Unit',
        copy=False,
    )
