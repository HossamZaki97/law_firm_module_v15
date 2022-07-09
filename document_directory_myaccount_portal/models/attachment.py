# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Attachment(models.Model):
    _inherit = 'ir.attachment'
    
    partner_ids = fields.Many2many(
        'res.partner',
        string = "Share on Portal"
    )
    custom_global = fields.Boolean(
    	string='Share Globaly', 
	)