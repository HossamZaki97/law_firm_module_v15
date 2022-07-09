# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class AccountInvoice(models.Model):
#    _inherit = 'account.invoice'
    _inherit = 'account.move'

    job_cost_id = fields.Many2one(
        'job.costing',
        readonly=True,
        string="Job Cost Sheet",
    )


class AccountInvoiceLine(models.Model):
    _inherit = 'account.move.line'

    job_cost_line_ids = fields.Many2many(
        'job.cost.line',
        'job_cost_line_invoice_rel',
        'invoice_line_id', 'job_cost_line_id',
        string='Job Cost Lines',
        readonly=True,
        copy=False
    )
