# -*- coding: utf-8 -*-

from odoo import models, fields

class DirectoryTag(models.Model):
    _name = 'directory.tag'
    _description = 'Directory Tags'
    
    name = fields.Char(
        string='Name',
        required=True,
    )
    color = fields.Integer(
        string='Color Index'
    )