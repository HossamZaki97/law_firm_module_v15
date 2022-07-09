# -*- coding: utf-8 -*-

from odoo import models, fields, api

class CaseCourt(models.Model):
    _name = "case.court"

    name = fields.Char(
        string="Name",
        required=True
    )
    partner_id = fields.Many2one(
        'res.partner',
        string="Address"
    )
