# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ProjectProject(models.Model):
    _inherit = "project.project"

    def custom_show_get_my_billing_invoices(self):
        self.ensure_one()
        project_ids = self.env['account.move'].sudo().search([])
        res = self.env.ref('account.action_move_out_invoice_type')
        res = res.read()[0]
        res['domain'] = str([('project_id','=',self.analytic_account_id.id)])
        return res