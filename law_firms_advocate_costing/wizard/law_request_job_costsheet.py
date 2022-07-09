# -*- coding: utf-8 -*-


from odoo import models, fields, api, _
from odoo.exceptions import Warning


class LawRequestJobCostSheetWizard(models.TransientModel):
    _name = "law.request.jobcostsheet.wizard"
    
    costsheet_type = fields.Selection(
        [('create_costsheet','Create Job Cost Sheet'),
         ('update_costsheet','Update Job Cost Sheet')],
        string='Cost Sheet Options',
        default='create_costsheet',
        required=True,
    )
    job_costsheet_id = fields.Many2one(
        'job.costing',
        string='Job Cost Sheet',
    )
    project_id = fields.Many2one(
        'project.project',
        string='Project',
        readonly=True
    )
    task_id = fields.Many2one(
        'project.task',
        string='Job Order',
    )

    @api.model
    def default_get(self, fields):
        res = super(LawRequestJobCostSheetWizard, self).default_get(fields)
        active_id = dict(self._context or {}).get('active_id', False)
        record = self.env['project.project'].browse(active_id)
        res.update({
            'project_id': record.id,
        })
        return res

    def custom_create_edit_jobcostsheet(self):
        material_vals_list = []
        labour_vals_list = []
        overhead_vals_list = []
        custom_material_vals_list = []
        custom_labour_vals_list = []
        custom_overhead_vals_list = []
        context = dict(self._context or {})
        active_id = self.env['project.project'].browse(context.get('active_id', False))
        if self.costsheet_type == 'create_costsheet':
            for material_line in active_id.material_jobcost_line_ids:
                if material_line.is_create_custom_line != True:
                    material_lines = (0,0,{
                        'date': material_line.date,
                        'job_type_id': material_line.job_type_id.id,
                        'job_type' : 'material',
                        'product_id': material_line.product_id.id,
                        'product_qty': material_line.product_qty,
                        'uom_id': material_line.uom_id.id,
                        'description': material_line.product_id.name,
                        'cost_price': material_line.cost_price,
                        'law_job_cost_line': material_line.id
                        })
                    material_vals_list.append(material_lines)
                    material_line.write({
                        'is_create_custom_line': True,
                        })
            for labour_line in active_id.labour_jobcost_line_ids:
                if labour_line.is_create_custom_line != True:
                    labour_lines = (0,0,{
                        'date': labour_line.date,
                        'job_type_id': labour_line.job_type_id.id,
                        'job_type' : 'labour',
                        'product_id': labour_line.product_id.id,
                        'hours': labour_line.hours,
                        'cost_price': labour_line.cost_price,
                        'description': labour_line.product_id.name,
                        'law_job_cost_line': labour_line.id
                        })
                    labour_vals_list.append(labour_lines)
                    labour_line.write({
                        'is_create_custom_line': True,
                        })
            for overhead_line in active_id.overhead_jobcost_line_ids:
                if overhead_line.is_create_custom_line != True:
                    overhead_lines = (0,0,{
                        'date': overhead_line.date,
                        'job_type_id': overhead_line.job_type_id.id,
                        'job_type' : 'overhead',
                        'product_id': overhead_line.product_id.id,
                        'product_qty': overhead_line.product_qty,
                        'uom_id': overhead_line.uom_id.id,
                        'cost_price': overhead_line.cost_price,
                        'description': overhead_line.product_id.name,
                        'law_job_cost_line': overhead_line.id
                        })
                    overhead_vals_list.append(overhead_lines)
                    overhead_line.write({
                        'is_create_custom_line': True,
                        })
            action = self.env.ref('odoo_job_costing_management.action_job_costing').read()[0]
            action['views'] = [(self.env.ref('odoo_job_costing_management.job_costing_form_view').id, 'form')]
            action['context'] = {
                'default_name':'New',
                'default_analytic_id': active_id.analytic_account_id.id,
                'default_partner_id': active_id.partner_id.id,
                'default_task_id': self.task_id.id,
                'default_job_cost_line_ids': material_vals_list,
                'default_job_labour_line_ids': labour_vals_list,
                'default_job_overhead_line_ids': overhead_vals_list,
                'default_project_id' : active_id.id,
            }
            return action
        if self.costsheet_type == 'update_costsheet':
            for custom_material_line in active_id.material_jobcost_line_ids:
                if custom_material_line.is_create_custom_line != True:
                    custom_material_lines = (0,0,{
                        'date': custom_material_line.date,
                        'job_type_id': custom_material_line.job_type_id.id,
                        'job_type' : 'material',
                        'product_id': custom_material_line.product_id.id,
                        'product_qty': custom_material_line.product_qty,
                        'uom_id': custom_material_line.uom_id.id,
                        'cost_price': custom_material_line.cost_price,
                        'description': custom_material_line.product_id.name,
                        'law_job_cost_line': custom_material_line.id
                        })
                    custom_material_vals_list.append(custom_material_lines)
                    custom_material_line.write({
                        'is_create_custom_line': True,
                    })
            for custom_labour_line in active_id.labour_jobcost_line_ids:
                if custom_labour_line.is_create_custom_line != True:
                    custom_labour_lines = (0,0,{
                        'date': custom_labour_line.date,
                        'job_type_id': custom_labour_line.job_type_id.id,
                        'job_type' : 'labour',
                        'product_id': custom_labour_line.product_id.id,
                        'hours': custom_labour_line.hours,
                        'cost_price': custom_labour_line.cost_price,
                        'description': custom_labour_line.product_id.name,
                        'law_job_cost_line': custom_labour_line.id
                        })
                    custom_labour_vals_list.append(custom_labour_lines)
                    custom_labour_line.write({
                        'is_create_custom_line': True,
                    })
            for custom_overhead_line in active_id.overhead_jobcost_line_ids:
                if custom_overhead_line.is_create_custom_line != True:
                    custom_overhead_lines = (0,0,{
                        'date': custom_overhead_line.date,
                        'job_type_id': custom_overhead_line.job_type_id.id,
                        'job_type' : 'overhead',
                        'product_id': custom_overhead_line.product_id.id,
                        'product_qty': custom_overhead_line.product_qty,
                        'uom_id': custom_overhead_line.uom_id.id,
                        'cost_price': custom_overhead_line.cost_price,
                        'description': custom_overhead_line.product_id.name,
                        'law_job_cost_line': custom_overhead_line.id
                        })
                    custom_overhead_vals_list.append(custom_overhead_lines)
                    custom_overhead_line.write({
                        'is_create_custom_line': True,
                    })
            self.job_costsheet_id.update({
                'job_cost_line_ids': custom_material_vals_list,
                'job_labour_line_ids': custom_labour_vals_list,
                'job_overhead_line_ids': custom_overhead_vals_list,
                })
            action = self.env.ref('odoo_job_costing_management.action_job_costing').read()[0]
            action['domain'] = [('id','=', self.job_costsheet_id.id)]
            return action