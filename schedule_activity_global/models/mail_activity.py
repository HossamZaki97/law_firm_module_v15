# -*- coding: utf-8 -*-

from odoo import models, fields, api

class MailActivity(models.Model):

    _inherit = 'mail.activity'

    supervisor_user_id = fields.Many2one(
        'res.users',
        string='Supervisor',
        copy=False,
    )

    def name_get(self):
        res = []
        for record in self:
            if self._context.get('view_type') == 'calendar' or True:
                summary = record.summary or ''
                if summary:
                    name = record.res_name + '-' + summary or record.activity_type_id.display_name
                else:
                    name = record.res_name or record.activity_type_id.display_name
                res.append((record.id, name))
            else:
                name = record.summary or record.activity_type_id.display_name
                res.append((record.id, name))
        return res
    
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
