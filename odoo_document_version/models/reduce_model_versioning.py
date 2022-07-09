# -*- coding: utf-8 -*-

# Part of Probuse Consulting Service Pvt Ltd. See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api


class ReduceModelVersioning(models.Model):
    _name = "reduce.model.versioning"
    _description = "Document Version"

    name = fields.Char(
        string='Name',
        required=True,
    )
    company_id = fields.Many2one(
        'res.company',
        string='Company',
        required=True,
    )
    res_model_ids = fields.Many2many(
        'ir.model',
        string='Models',
    )
