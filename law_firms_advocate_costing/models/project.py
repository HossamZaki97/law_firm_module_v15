# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime, timedelta

class ProjectProject(models.Model):
    _inherit = "project.project"

    material_jobcost_line_ids = fields.One2many(
        'law.jobcost.line',
        'project_id',
        string="Material Cost Line",
        copy=True,
        domain=[('job_type','=','material')],
    )
    labour_jobcost_line_ids = fields.One2many(
        'law.jobcost.line',
        'project_id',
        string="Labour Cost Line",
        copy=True,
        domain=[('job_type','=','labour')],
    )
    overhead_jobcost_line_ids = fields.One2many(
        'law.jobcost.line',
        'project_id',
        string="Overhead Cost Line",
        copy=True,
        domain=[('job_type','=','overhead')],
    )
    
    def show_jobcost_sheet(self):
        self.ensure_one()
        action = self.env.ref("odoo_job_costing_management.action_job_costing").read()[0]
        action['domain'] = [('project_id','=', self.id)]
        return action