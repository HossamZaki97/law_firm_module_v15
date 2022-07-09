# -*- coding: utf-8 -*-

from odoo import models, fields, api

class HrEmployee(models.Model):
    _inherit = "hr.employee"

    custom_is_lawyer = fields.Boolean(
        string="Is Lawyer"
    )

