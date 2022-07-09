# -*- coding: utf-8 -*-

from odoo import models, fields, api,_

class ProjectProject(models.Model):
    _inherit = "project.project"

    custom_cases_doc_count = fields.Integer(
        compute='_compute_attached_cases_docs_count', 
        string="Number of documents attached",
    )
    
    def _compute_attached_cases_docs_count(self):
        Attachment = self.env['ir.attachment']
        for project in self:
            project.custom_cases_doc_count = Attachment.search_count([
                ('res_model', '=', 'project.project'), ('res_id', '=', project.id)
            ])
    
    def cases_attachment_view(self):
        self.ensure_one()
        domain = [('res_model', '=', 'project.project'), ('res_id', 'in', self.ids)]
        return {
            'name': _('Documents'),
            'domain': domain,
            'res_model': 'ir.attachment',
            'type': 'ir.actions.act_window',
            'view_id': False,
            'view_mode': 'kanban,tree,form',
            'help': _('''<p class="oe_view_nocontent_create">
                        Documents are attached to the job costing.</p><p>
                        Send messages or log internal notes with attachments to link
                        documents to your Job Cost Sheet.
                    </p>'''),
            'limit': 80,
            'context': "{'default_res_model': '%s','default_res_id': %d}" % (self._name, self.id)
        }

