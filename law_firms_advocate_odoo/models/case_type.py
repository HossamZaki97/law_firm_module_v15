# -*- coding: utf-8 -*-

from odoo import models, fields, api

class CaseType(models.Model):
    _name = "case.type"

    name = fields.Char(
        string="Name",
        required=True
    )
    abbreviated_form = fields.Char(
        string="Abbreviated Form",
        required=True
    )

    def name_get(self):
        result = []
        for rec in self:
            name = rec.abbreviated_form + ' - ' + rec.name
            result.append((rec.id, name))
        return result
