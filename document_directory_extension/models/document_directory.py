# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

class DocumentDirectory(models.Model):
    _name = 'document.directory'
    _description = 'Directory'
    _order = 'id desc'
    
    name = fields.Char(
        string='Directory Name',
        required=True,
    )
    parent_id = fields.Many2one(
        'document.directory',
        string='Parent Directory'
    )
    model_id = fields.Many2one(
        'ir.model',
        string='Model',
#         required=True,
    )
    attachment_count = fields.Integer(
        compute="_compute_attachment",
        #store=True,
     )
    children_ids = fields.One2many(
        'document.directory',
        'parent_id',
        string="Childs",
    )
    attachment_ids = fields.One2many(
        'ir.attachment',
        'directory_id',
        string="Attachments",
    )
    code = fields.Char(
        string='Directory Code',
        required=True,
    )
    sequence_id = fields.Many2one(
        'ir.sequence',
        string='Entry Sequence',
        readonly=True,
    )
    group_ids = fields.Many2many(
        'res.groups',
        string='Groups',
    )
    dir_type = fields.Selection(
        [('view','View'),
         ('dir','Directory')],
        string='Type',
        default='dir',
    )

    res_id = fields.Integer(
        string="Resource ID",
    )

    @api.depends()
    def _compute_attachment(self):
        for rec in self:
            child_doc_ids = self.env['document.directory'].sudo().search([('parent_id', '=', rec.id)])
            doc_ids = child_doc_ids + rec
            attachment = self.env['ir.attachment'].sudo().search_count([('directory_id', 'in', doc_ids.ids)])
            rec.attachment_count = attachment

    #@api.one
    @api.constrains('parent_id')
    def _check_container(self):
        if self.parent_id.name == self.name:
            raise ValidationError(_('Please select Different Parent Directory.'))
       
#    @api.one
#    @api.constrains('model_id')
#    def _check_model(self):
#        model = self.env['document.directory'].sudo().search([('model_id.model', '=', self.model_id.model)])
#        if len(model) == 2:
#            raise ValidationError(_('Directory for this model is already created!'))

    #@api.one
    @api.constrains('model_id','res_id')
    def _check_model(self):
        domain = [('model_id', '=', self.model_id.id)]
        print("domain-------------",domain)
        if self.res_id > 0:
            domain += [('res_id', '=', self.res_id)]
        else:
            domain += [('res_id', '=', False)]

        model = self.env['document.directory'].sudo().search(domain)
        if len(model) >= 2:
            raise ValidationError(_('Directory for this model is already created!'))
            
    #@api.multi
    def show_attachment(self):
#        for rec in self:
#        saler = self.env['ir.attachment']
        self.ensure_one()
        child_doc_ids = self.env['document.directory'].sudo().search([('parent_id', '=', self.id)])
        doc_ids = child_doc_ids + self
        res = self.env.ref('base.action_attachment')
        res = res.read()[0]
        res['domain'] = str([('directory_id', 'in', doc_ids.ids)])
        return res
        
    @api.model
    def create(self,vals):
        pre_val = vals.get('code' ,False)
        name = vals.get('name' ,False)
        vals1 = {
            'code' : pre_val,
            'name': name,
            'prefix' : pre_val+'/',
            'padding' : 4,
            }
        seq_obj=self.env['ir.sequence'].sudo().create(vals1)
        vals.update({
            'sequence_id': seq_obj.id
            })
        result = super(DocumentDirectory, self).create(vals)
        return result
        
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
