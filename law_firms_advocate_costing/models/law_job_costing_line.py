# -*- coding: utf-8 -*-

# Part of Probuse Consulting Service Pvt Ltd. See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api


class LawJobCostLine(models.Model):
    _name = "law.jobcost.line"
    _description = "Law JobCost Line"
    
    @api.onchange('product_id')
    def _onchange_product_id(self):
        for rec in self:
            rec.description = rec.product_id.name
            rec.product_qty = 1.0
            rec.uom_id = rec.product_id.uom_id.id
            rec.cost_price = rec.product_id.standard_price

    project_id = fields.Many2one(
        'project.project',
        string='Project',
        readonly=True
    )
    date = fields.Date(
        string="Date",
        required=True
    )
    job_type = fields.Selection(
        selection=[
                    ('material','Material'),
                    ('labour','Labour'),
                    ('overhead','Overhead')
                ],
        string="Type",
        required=True
    )
    job_type_id = fields.Many2one(
        'job.type',
        string="Job Type"
    )
    product_id = fields.Many2one(
        'product.product',
        string="Product",
        required=True
    )
    description = fields.Char(
        string="Description"
    )
    uom_id = fields.Many2one(
        'uom.uom',
        string='Unit of Measure',
    )
    product_qty = fields.Float(
        string="Quantity",
    )
    cost_price = fields.Float(
        string='Cost / Unit',
        related='product_id.standard_price',
        store=True,
        digits='Product Price',
    )
    currency_id = fields.Many2one(
        'res.currency',
        string="Currency",
        default=lambda self: self.env.user.company_id.currency_id, 
        readonly=True
    )
    hours = fields.Float(
        string='Hours'
    )
    is_create_custom_line = fields.Boolean(
        string="Job Cost Sheet Created?",
        readonly=True,
        copy=False
    )

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
