# -*- coding: utf-8 -*-

from odoo import models, fields, api

class AccountAnalytic(models.Model):
    _inherit = 'account.analytic.account'

    total_progress_account = fields.Float(
        string="Total Progress Billing",
        copy=False,
    )
    
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
