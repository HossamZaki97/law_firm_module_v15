# -*- coding: utf-8 -*-

# Part of Probuse Consulting Service Pvt Ltd. See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api
from odoo.addons import decimal_precision as dp

class MailThread(models.AbstractModel):
    _inherit = 'mail.thread'

    # @api.multi
    # def _message_post_process_attachments(self, attachments, attachment_ids, message_data):
    #     res = super(MailThread, self)._message_post_process_attachments(attachments, attachment_ids, message_data)
        
    #     IrAttachment = self.env['ir.attachment']
    #     ir_attachment = self.env['ir.attachment']
    #     for attachment in IrAttachment.browse(attachment_ids):
    #         # if len(attachment) == 2:
    #         #     name, content = attachment
    #         # elif len(attachment) == 3:
    #         #     name, content, info = attachment
    #         #     cid = info and info.get('cid')
    #         # else:
    #         #     continue
    #         ir_attachment = self.env['ir.attachment']
    #         if attachment.name:#vals.get("datas_fname"):

    #             # ('datas_fname', '=', vals.get("datas_fname"))
                
    #             ir_attachment = IrAttachment.search([
    #                 ('name', '=', attachment.name),
    #                 ('res_model','=',message_data['model']),
    #                 ('res_id','=',message_data['res_id'])], 
    #                 order="id desc",
    #                 # limit=1
    #             )

    #             ids_att = ir_attachment.ids
    #             ids_att.remove(attachment.id)
    #             if ids_att:
    #                 ir_attachment = max(ids_att)
    #                 ir_attachment = IrAttachment.browse(ir_attachment)
    #             else:
    #                 ir_attachment = attachment
    #             # ir_attachment = max(ids_att) = ir_attachment[0]
    #         config = self.env['reduce.model.versioning'].sudo().search([
    #             ('company_id', '=', self.env.user.company_id.id)
    #         ], limit=1)
    #         if config:
    #             search_model = self.env['ir.model'].search([
    #                 ('model', '=', message_data['model'])
    #             ])
    #             if search_model.id in config.res_model_ids.ids:
    #                 # return super(IrAttachment, self).create(vals)
    #                 pass
    #             else:
    #                 if ir_attachment:
    #                     custom_version = ir_attachment.custom_version + 1
    #                     attachment.update({
    #                             'prev_attachment_id': ir_attachment.id,
    #                             'custom_version': custom_version,
    #                         })
    #         else:
    #             if ir_attachment:
    #                 custom_version = ir_attachment.custom_version + 1
    #                 attachment.update({
    #                         'prev_attachment_id': ir_attachment.id,
    #                         'custom_version': custom_version,
    #                     })
    #         # attachment_id = super(IrAttachment, self).create(vals)
    #     if ir_attachment:
    #         ir_attachment.write({
    #             'new_attachment_id': attachment.id
    #         })
    #     return res


class IrAttachment(models.Model):
    _inherit = "ir.attachment"

    prev_attachment_id = fields.Many2one(
        'ir.attachment',
        string='Previous Version Document',
        readonly=False,
        copy=False,
    )
    new_attachment_id = fields.Many2one(
        'ir.attachment',
        string='New Version Document',
        readonly=True,
        copy=False,
    )
    custom_version = fields.Float(
        string="Document Version",
        copy=False,
        default=0.0,
        digits=(4, 1),
    )
    custom_display_name = fields.Char(
        string="Displayed Name", compute='_custom_version'
    )

#    @api.multi
    @api.depends('custom_version','name')
    def _custom_version(self):
        for record in self:
            for rec in record:
                rec.custom_display_name = (rec.name or '')+'('+ str(rec.custom_version or '') + ')'
               

 #   @api.multi
    def action_previous_version(self):
        self.ensure_one()
        res = self.env.ref('base.action_attachment')
        res = res.read()[0]
        res['domain'] = str([('id','=',self.prev_attachment_id.id)])
        return res

  #  @api.multi
    def action_next_version(self):
        self.ensure_one()
        res = self.env.ref('base.action_attachment')
        res = res.read()[0]
        res['domain'] = str([('id','=',self.new_attachment_id.id)])
        return res

    @api.model#this will not work with odoo 12 ? mustufa rangwala - unused method.. 
    def search_read_dummy_notused(self, domain=None,
            fields=None, offset=0, limit=None, order=None):
        attachment_obj = self
        result = super(IrAttachment, self).search_read(
            domain=domain, fields=fields,
            offset=offset, limit=limit,
            order=order
        )
        action = self.env.ref("base.action_attachment")

        config = self.env['reduce.model.versioning'].sudo().search([
            ('company_id', '=', self.env.user.company_id.id)],
            limit=1
        )

        if 'params' in self._context:
            if 'action' in self._context['params']:
                action_record = self.env['ir.actions.act_window'].browse(
                    self._context['params']['action']
                )
                res_my_model = action_record.res_model

                if config:
                    search_model = self.env['ir.model'].search(
                        [('model', '=', res_my_model)]
                    )
                    if search_model.id in config.res_model_ids.ids:
                        return result

        if self._context.get("params") and self._context['params'].get("action"):
            if not self._context['params']['action'] == action.id:
                for attach in result:
                    if attach.get("id") and attach.get("name"):
                        attachment_id = attachment_obj.browse(attach.get("id"))
                        custom_version = attachment_id.custom_version
                        attach['name'] = attach['name'] + " (" + str(custom_version )+")"
        return result
        
    def _get_custom_version_document(self, ir_attachment):
        custom_version = ir_attachment.custom_version + 1
        return custom_version

    #@api.model
    #def create(self,vals):
    @api.model_create_multi
    def create(self, vals_list):
        #attachment = super(Attachment, self).create(vals)
        attachments = super(IrAttachment, self).create(vals_list)
        ir_attachment = self.env['ir.attachment']
        for attachment in attachments:
            if attachment.name:#vals.get("datas_fname"):

                # ('datas_fname', '=', vals.get("datas_fname"))
                ir_attachment = self.env['ir.attachment'].search([
                    ('name', '=', attachment.name),
                    ('res_model','=',attachment.res_model),
                    ('res_id','=',attachment.res_id)],
                    order="id desc"
                    # limit=1
                )
                ids_att = ir_attachment.ids
                if attachment.id in ids_att:
                    ids_att.remove(attachment.id)
                if ids_att:
                    ir_attachment = max(ids_att)
                    ir_attachment = self.env['ir.attachment'].browse(ir_attachment)
                else:
                    ir_attachment = attachment
                # ir_attachment = max(ids_att) = ir_attachment[0]
            config = self.env['reduce.model.versioning'].sudo().search([
                ('company_id', '=', self.env.user.company_id.id)
            ], limit=1)
            if config:
                search_model = self.env['ir.model'].search([
                    ('model', '=', attachment.res_model)
                ])
                if search_model.id in config.res_model_ids.ids:
                    # return super(IrAttachment, self).create(vals)
                    pass

                else:
                    if ir_attachment:
    #                    custom_version = ir_attachment.custom_version + 1
                        custom_version = attachment._get_custom_version_document(ir_attachment)
                        attachment.update({
                                'prev_attachment_id': ir_attachment.id,
                                'custom_version': custom_version,
                            })
            else:
                if ir_attachment:
    #                custom_version = ir_attachment.custom_version + 1
                    custom_version = attachment._get_custom_version_document(ir_attachment)
                    attachment.update({
                            'prev_attachment_id': ir_attachment.id,
                            'custom_version': custom_version,
                        })
            # attachment_id = super(IrAttachment, self).create(vals)
            if ir_attachment:
                ir_attachment.write({
                    'new_attachment_id': attachment.id
                })
        return attachments


   # @api.multi
    def write(self, vals):
        res = super(IrAttachment, self).write(vals)
        if 'res_model' in vals and 'res_id' in vals:
            ir_attachment = self.env['ir.attachment']
            for attachment in self:
                if attachment.name:#vals.get("datas_fname"):

                    # ('datas_fname', '=', vals.get("datas_fname"))
                    ir_attachment = self.env['ir.attachment'].search([
                        ('name', '=', attachment.name),
                        ('res_model','=',attachment.res_model),
                        ('res_id','=',attachment.res_id)], 
                        order="id desc"
                        # limit=1
                    )
                    ids_att = ir_attachment.ids
                    if attachment.id in ids_att:
                        ids_att.remove(attachment.id)
                    if ids_att:
                        ir_attachment = max(ids_att)
                        ir_attachment = self.env['ir.attachment'].browse(ir_attachment)
                    else:
                        ir_attachment = attachment
                    # ir_attachment = max(ids_att) = ir_attachment[0]
                config = self.env['reduce.model.versioning'].sudo().search([
                    ('company_id', '=', self.env.user.company_id.id)
                ], limit=1)
                if config:
                    search_model = self.env['ir.model'].search([
                        ('model', '=', attachment.res_model)
                    ])
                    if search_model.id in config.res_model_ids.ids:
                        # return super(IrAttachment, self).create(vals)
                        pass
                    else:
                        if ir_attachment:
                            # custom_version = ir_attachment.custom_version + 1
                            custom_version = attachment._get_custom_version_document(ir_attachment)
                            attachment.update({
                                    'prev_attachment_id': ir_attachment.id,
                                    'custom_version': custom_version,
                                })
                else:
                    custom_version = 1.0
                    if ir_attachment:
                        if ir_attachment.id != attachment.id:
                            # custom_version = ir_attachment.custom_version + 1
                            custom_version = attachment._get_custom_version_document(ir_attachment)
                        attachment.update({
                                'prev_attachment_id': ir_attachment.id,
                                'custom_version': custom_version,
                            })
                # attachment_id = super(IrAttachment, self).create(vals)
                if ir_attachment:
                    ir_attachment.write({
                        'new_attachment_id': attachment.id
                    })
        return res

    # @api.model
    # def create(self, vals):
    #     ir_attachment = self
    #     if vals.get("datas_fname"):

    #         ('datas_fname', '=', vals.get("datas_fname"))

    #         ir_attachment = self.search([
    #             ('datas_fname', '=', vals.get("datas_fname")),
    #             ('res_model','=',vals.get("res_model")),
    #             ('res_id','=',vals.get("res_id"))], 
    #             order="id desc",
    #             limit=1
    #         )

    #         config = self.env['reduce.model.versioning'].sudo().search([
    #             ('company_id', '=', self.env.user.company_id.id)
    #         ], limit=1)
    #         if config:
    #             search_model = self.env['ir.model'].search([
    #                 ('model', '=', vals.get("res_model"))
    #             ])
    #             if search_model.id in config.res_model_ids.ids:
    #                 return super(IrAttachment, self).create(vals)
    #             else:
    #                 if ir_attachment:
    #                     custom_version = ir_attachment.custom_version + 1
    #                     vals.update({
    #                             'prev_attachment_id': ir_attachment.id,
    #                             'custom_version': custom_version,
    #                         })
    #         else:
    #             if ir_attachment:
    #                 custom_version = ir_attachment.custom_version + 1
    #                 vals.update({
    #                         'prev_attachment_id': ir_attachment.id,
    #                         'custom_version': custom_version,
    #                     })
    #     attachment_id = super(IrAttachment, self).create(vals)
    #     if ir_attachment:
    #         ir_attachment.write({
    #             'new_attachment_id': attachment_id.id
    #         })
    #     return attachment_id

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: