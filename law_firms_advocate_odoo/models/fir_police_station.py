# -*- coding: utf-8 -*-

from odoo import models, fields, api

class FirPoliceStation(models.Model):
    _name = "fir.police.station"

    name = fields.Char(
        string="Name",
        required=True
    )
    partner_id = fields.Many2one(
        'res.partner',
        string="Address"
    )
