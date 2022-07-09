# -*- coding: utf-8 -*-

from odoo import api, fields, models, _


class Task(models.Model):
    _inherit = "project.task"
    
    doc_count = fields.Integer(
        compute='compute_attached_document', 
        string="Number of documents attached",
        # store=True,
    )
    
    def compute_attached_document(self):
        Attachment = self.env['ir.attachment']
        for task in self:
            task.doc_count = Attachment.search_count([
                ('res_model', '=', 'project.task'), ('res_id', '=', task.id)
            ])
    
    # @api.multi
    def attachment_projecttree_view(self):
        self.ensure_one()
        domain = [('res_model', '=', 'project.task'), ('res_id', 'in', self.ids)]
        return {
            'name': _('Attachments'),
            'domain': domain,
            'res_model': 'ir.attachment',
            'type': 'ir.actions.act_window',
            'view_id': False,
            'view_mode': 'kanban,tree,form',
            # 'view_type': 'form',
            'help': _('''<p class="oe_view_nocontent_create">
                        Documents are attached to the job order / task project.</p><p>
                        Send messages or log internal notes with attachments to link
                        documents to your project.
                    </p>'''),
            'limit': 80,
            'context': "{'default_res_model': '%s','default_res_id': %d}" % (self._name, self.id)
        }