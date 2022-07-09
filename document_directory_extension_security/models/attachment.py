# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Attachment(models.Model):
    _inherit = 'ir.attachment'
    
    @api.depends('directory_id',
                 'directory_id.user_ids')
    def compute_user_ids(self):
        for rec in self:
            rec.user_ids = rec.directory_id.user_ids.ids
    
    @api.depends('directory_id',
                 'directory_id.tag_ids')
    def compute_directory_tags(self):
        for rec in self:
            rec.dirctory_tag_ids = rec.directory_id.tag_ids.ids
    
    user_ids = fields.Many2many(
        'res.users',
        string='Users',
        compute='compute_user_ids',
        store=True,
    )
    tag_ids = fields.Many2many(
        'attachment.tag',
        string='Attachment Tags',
    )
    dirctory_tag_ids = fields.Many2many(
        'directory.tag',
        string='Directory Tags',
        compute='compute_directory_tags',
        store=True,
    )
    
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
