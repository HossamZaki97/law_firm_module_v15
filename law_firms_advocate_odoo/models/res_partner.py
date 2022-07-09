# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ResPartner(models.Model):
    _inherit = "res.partner"

    custom_is_witnes = fields.Boolean(
        string="Is Witness"
    )
