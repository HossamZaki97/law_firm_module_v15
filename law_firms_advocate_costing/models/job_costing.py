# -*- coding: utf-8 -*-

# Part of Probuse Consulting Service Pvt Ltd. See LICENSE file for full copyright and licensing details.

from odoo import models, fields

class JobCostLine(models.Model):
    _inherit = "job.cost.line"
    
    law_job_cost_line = fields.Many2one(
        'law.jobcost.line',
        string="Law JobCost Line",
        copy=False
    )

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
