# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime, timedelta
import logging
_logger = logging.getLogger(__name__)

class ProjectProject(models.Model):
    _inherit = "project.project"


    custom_case_number = fields.Char(
        'CNR Number', 
    )
    custom_case_file_number = fields.Char(
        'Filing Number', 
    )
    custom_opposite_client = fields.Many2one(
        'res.partner',
        string='Opposite Client', 
    )
    custom_opposite_advocate = fields.Many2one(
        'res.partner',
        string='Opposite Advocate', 
    )
    custom_case_description = fields.Html(
        'Case Details', 
    )
    customer_case_file_date = fields.Date(
        string="Case File Date",
        default=fields.Date.today()
    )
    custom_case_type_id = fields.Many2one(
        'case.type',
        string="Case Type"
    )
    custom_lawyer_ids = fields.Many2many(
        'hr.employee',
        domain=[('custom_is_lawyer','=',True)],
        string="Lawyers"
    )
    custom_witness_ids = fields.Many2many(
        'res.partner',
        'case_witness_id',
        'case_id',
        domain=[('custom_is_witnes','=',True)],
        string="Witness"
    )
    is_law_firm_project = fields.Boolean(
        string="Is Law Firm Project"
    )
    custom_fir_number = fields.Char(
        string="FIR Number"
    )
    custom_fir_police_station_id = fields.Many2one(
        'fir.police.station',
        string="FIR Police Station"
    )
    custom_po_station_add_id = fields.Many2one(
        'res.partner',
        related='custom_fir_police_station_id.partner_id',
        string="Station Address"
    )
    custom_court_id = fields.Many2one(
        'case.court',
        string='Court'
    )
    custom_court_add_id = fields.Many2one(
        'res.partner',
        related='custom_court_id.partner_id',
        string="Court Address"
    )
    custom_next_hearing_date = fields.Date(
        string="Next Hearing Date"
    )
    custom_hearing_alrt_days = fields.Integer(
        string='Hearing Reminder Notification',
        default='3'
    )

    def custom_get_lawyers_value(self):
        lawyer_name = ''
        if self.custom_lawyer_ids:
            for lawyer in self.custom_lawyer_ids:
                if lawyer_name == '':
                    lawyer_name = lawyer.name
                else:
                    lawyer_name = lawyer_name + ' , ' + lawyer.name
        return lawyer_name

    def custom_get_witness_value(self):
        witness_name = ''
        if self.custom_witness_ids:
            for witnes in self.custom_witness_ids:
                if witness_name == '':
                    witness_name = witnes.name
                else:
                    witness_name = witness_name + ' , ' + witnes.name
        return witness_name

    def custom_show_get_my_cases_sale_order(self):
        for rec in self:
            res = self.env.ref('sale.action_quotations_with_onboarding')
            res = res.read()[0]
            sale_ids = self.env['sale.order'].search([('project_id', '=', self.id)]).ids
            res['domain'] = str([('id', 'in', sale_ids)])
        return res

    def custom_show_get_my_cases_invoice(self):
        for rec in self:
            res = self.env.ref('account.action_move_out_invoice_type')
            res = res.read()[0]
            sale_ids = self.env['sale.order'].search([('project_id', '=', self.id)]).ids
            invoice_ids = self.env['account.move']
            for order in sale_ids:
                invoice_ids += order.invoice_ids
            res['domain'] = str([('id', 'in', invoice_ids.ids)])
        return res        

    def custom_show_get_my_cases_task(self):
        for rec in self:
            res = self.env.ref('')

    def _cron_case_hearing_notification_mail(self):
        project_ids = self.env['project.project'].search([('is_law_firm_project', '=', True)])
        for project in project_ids:
            today_date = fields.Date.today()
            notification_date = today_date + timedelta(project.custom_hearing_alrt_days)
            task_id = self.env['project.task'].search([
                ('project_id', '=', project.id),
                ('custom_next_hearing_date', '=', project.custom_next_hearing_date)
            ], order='custom_next_hearing_date desc', limit=1)
            template = self.env.ref('law_firms_advocate_odoo.email_template_hearing_notification_mail')
            if project.custom_next_hearing_date == notification_date:
                if task_id:
                    template.sudo().with_context({
                        'receiver_email': task_id.user_id.email,
                        'receiver_name': task_id.user_id.name}).send_mail(task_id.id)
                    template.sudo().with_context({
                        'receiver_email': project.partner_id.email,
                        'receiver_name': project.partner_id.name}).send_mail(task_id.id)

class ProjectTask(models.Model):
    _inherit = "project.task"

    is_law_firm_task = fields.Boolean(
        string="Is Law Firm Task",
    )
    custom_last_hearing_date = fields.Date(
        string="Last Hearing Date"
    )
    custom_hearing_date = fields.Date(
        string="Hearing Date",
        default=fields.Date.today()
    )
    custom_next_hearing_date = fields.Date(
        string="Next Hearing Date"
    )
    custom_hearing_details = fields.Char(
        string="Purpose of Hearing"
    )

    def custom_get_custom_next_hearing_date(self, project, new_date=None):
        task_id = False
        custom_next_hearing_date = False
        if project:
            task_id = self.env['project.task'].search([('project_id', '=', project.id)], order='custom_next_hearing_date desc', limit=1)
        if task_id and task_id.custom_next_hearing_date:
            custom_next_hearing_date = task_id.custom_next_hearing_date
        if new_date:
            if task_id and task_id.custom_next_hearing_date:
                if new_date >= task_id.custom_next_hearing_date:
                    custom_next_hearing_date = new_date
            else:
                custom_next_hearing_date = new_date
        return custom_next_hearing_date

    @api.model
    def create(self, vals):
        res = super(ProjectTask, self).create(vals)
        if res.project_id and res.custom_next_hearing_date:
            custom_next_hearing_date = self.custom_get_custom_next_hearing_date(res.project_id, res.custom_next_hearing_date)
            res.project_id.custom_next_hearing_date = custom_next_hearing_date
        return res

    def write(self, vals):
        res = super(ProjectTask, self).write(vals)
        for rec in self:
            if vals.get('project_id') or vals.get('custom_next_hearing_date'):
                if vals.get('project_id'):
                    project_id = self.env['project.project'].browse(int(vals.get('project_id')))
                else:
                    project_id = rec.project_id
                if vals.get('custom_next_hearing_date'):
                    new_date =  datetime.strptime(vals.get('custom_next_hearing_date'), '%Y-%m-%d').date()
                    custom_next_hearing_date = self.custom_get_custom_next_hearing_date(project_id, new_date)
                else:
                    custom_next_hearing_date = self.custom_get_custom_next_hearing_date(project_id)
                project_id.custom_next_hearing_date = custom_next_hearing_date
        return res
