# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

class Attachment(models.Model):
    _inherit = 'ir.attachment'
    
    directory_id = fields.Many2one(
        'document.directory',
        string='Directory',
    )
    number = fields.Char(
        'Number', 
        copy=False,
        readonly=True,
    )
    
    #@api.multi
    def action_attachment_send(self):
        '''
        This function opens a window to compose an email, with the edi template message loaded by default
        '''
        self.ensure_one()
        ir_model_data = self.env['ir.model.data']
        try:
            template_id = ir_model_data.get_object_reference('document_directory_extension', 'email_template_document_attachment')[1]
        except ValueError:
            template_id = False
        try:
            compose_form_id = ir_model_data.get_object_reference('mail', 'email_compose_message_wizard_form')[1]
        except ValueError:
            compose_form_id = False
        ctx = dict()
        ctx.update({
            'default_model': 'ir.attachment',
            'default_res_id': self.ids[0],
            'default_use_template': bool(template_id),
            'default_template_id': template_id,
            'default_composition_mode': 'comment',
            'mark_so_as_sent': True,
#            'custom_layout': "mail_template_data_notification",
            'default_attachment_ids': [(6, 0, [self.id])] 
        })
        return {
            'type': 'ir.actions.act_window',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'mail.compose.message',
            'views': [(compose_form_id, 'form')],
            'view_id': compose_form_id,
            'target': 'new',
            'context': ctx,
        }

    #@api.model
    #def create(self,vals):
    @api.model_create_multi
    def create(self, vals_list):
        #attachment = super(Attachment, self).create(vals)
        attachment = super(Attachment, self).create(vals_list)
        model = attachment.res_model #vals.get('res_model',False)
        res_id = attachment.res_id #vals.get('res_id')
        if model:
            # directory = self.env['document.directory'].sudo().search([
            #     ('model_id.model', '=', model),
            #     '|',
            #     ('res_id','=',res_id),
            #     ('res_id','=',0)
            # ], limit=1)
            directory = self.env['document.directory'].sudo().search([
                ('model_id.model', '=', model),
                ('res_id','=',res_id),
            ], limit=1)
            if not directory:
                directory = self.env['document.directory'].sudo().search([
                ('model_id.model', '=', model),
                ('res_id','=',0)], limit=1)
            if directory.group_ids:
                flag= False
                for group in directory.group_ids:
                    external_id= group.get_external_id()[group.id]
                    if self.env.user.has_group(str(external_id)):
                        flag = True
                if not flag:
                    raise ValidationError(_("Sorry you don't have access for this document.'"))
            if directory:
                aname = attachment.name #vals.get('name', False)
                # vals['number'] = self.env['ir.sequence'].next_by_code(directory.sequence_id.code)
                attachment.number = self.env['ir.sequence'].next_by_code(directory.sequence_id.code)
                attachment.update({
                    'directory_id': directory.id
                })
                # vals.update({
                #     'directory_id': directory.id
                # })
            else:
                # vals['number'] = self.env['ir.sequence'].next_by_code('document.directory.seq')
                attachment.number = self.env['ir.sequence'].next_by_code('document.directory.seq')
        return attachment

    #@api.multi
    def write(self,vals):
        model = vals.get('res_model',False)
        res_id = vals.get('res_id', 0)
        if model and res_id:
            # directory = self.env['document.directory'].sudo().search([
            #     ('model_id.model', '=', model),
            #     '|',
            #     ('res_id','=',res_id),
            #     ('res_id','=',0)], limit=1)
            directory = self.env['document.directory'].sudo().search([
                ('model_id.model', '=', model),
                ('res_id','=',res_id),
            ], limit=1)
            if not directory:
                directory = self.env['document.directory'].sudo().search([
                ('model_id.model', '=', model),
                ('res_id','=',0)], limit=1)
            if directory.group_ids:
                flag= False
                for group in directory.group_ids:
                    external_id= group.get_external_id()[group.id]
                    if self.env.user.has_group(str(external_id)):
                        flag = True
                if not flag:
                    raise ValidationError(_("Sorry you don't have access for this document.'"))
            if directory:
                aname = vals.get('name', False)
                vals['number'] = self.env['ir.sequence'].next_by_code(directory.sequence_id.code)
                vals.update({
                    'directory_id': directory.id
                })
            else:
                vals['number'] = self.env['ir.sequence'].next_by_code('document.directory.seq')
        return super(Attachment, self).write(vals)

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
