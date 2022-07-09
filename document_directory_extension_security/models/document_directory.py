# -*- coding: utf-8 -*-

from odoo import models, fields

class DocumentDirectory(models.Model):
    _inherit = 'document.directory'
    
    user_ids = fields.Many2many(
        'res.users',
        string='Users',
    )
    tag_ids = fields.Many2many(
        'directory.tag',
        string='Tags',
    )
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
