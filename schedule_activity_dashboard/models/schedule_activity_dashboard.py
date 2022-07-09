# # -*- coding: utf-8 -*-
# Part of Probuse Consulting Service Pvt Ltd.
# See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api
import datetime
from datetime import timedelta
from datetime import datetime, timedelta, date
from dateutil.relativedelta import relativedelta


class ScheduleActivityDashboard(models.Model):
    _name = 'schedule_activity.dashboard'
    _order = 'sequence'

    cus_res_model_id = fields.Many2one(
        'ir.model',
        string='Model',
        required=True,
        ondelete='cascade'
    )
    sequence = fields.Integer(
        string="Sequence"
    )

#odoo13    @api.multi
    def action_today_activity(self):
        action = self.env.ref(
            'schedule_activity_dashboard.custom_action_smart_box'
        ).read()[0]
        action['context'] = {'search_default_activities_today': 1}
        action['domain'] = [('res_model_id', '=', self.cus_res_model_id.id)]
        return action

#odoo13    @api.multi
    def action_tomorrow_activity(self):
        action = self.env.ref(
            'schedule_activity_dashboard.custom_action_smart_box'
        ).read()[0]
        today = datetime.now()
        tomorrow_date = today + timedelta(days=1)
        action['domain'] = [('date_deadline', '=', tomorrow_date),
                            ('res_model_id', '=', self.cus_res_model_id.id)
                            ]
        return action

#odoo13    @api.multi
    def action_week_activity(self):
        action = self.env.ref(
            'schedule_activity_dashboard.custom_action_smart_box'
        ).read()[0]
        mail_activity = self.env['mail.activity']
        start_of_week = datetime.now() - \
            timedelta(days=datetime.now().weekday())
        end_of_week = start_of_week + timedelta(days=6)
        action['domain'] = [('date_deadline', '>=', start_of_week),
                            ('date_deadline', '<=', end_of_week),
                            ('res_model_id', '=', self.cus_res_model_id.id)
                            ]
        return action

#odoo13    @api.multi
    def action_yesterday_activity(self):
        action = self.env.ref(
            'schedule_activity_dashboard.custom_action_smart_box'
        ).read()[0]
        yesterday_date = date.today() - timedelta(days=1)
        action['domain'] = [('date_deadline', '=', yesterday_date),
                            ('res_model_id', '=', self.cus_res_model_id.id)
                            ]
        return action

#odoo13    @api.multi
    def action_month_activity(self):
        action = self.env.ref(
            'schedule_activity_dashboard.custom_action_smart_box'
        ).read()[0]
        today = date.today()
        start_of_month = today.replace(day=1)
        end_of_month = date(today.year , today.month, 1) + \
            relativedelta(months=1,days=-1)
        action['domain'] = [('date_deadline', '>=', start_of_month),
                            ('date_deadline', '<=', end_of_month),
                            ('res_model_id', '=', self.cus_res_model_id.id)
                            ]
        return action

#odoo13    @api.multi
    def action_last_month_activity(self):
        action = self.env.ref(
            'schedule_activity_dashboard.custom_action_smart_box'
        ).read()[0]
        today = date.today()
        end_date = today.replace(day=1) - relativedelta(days=1)
        start_date = end_date.replace(day=1)
        action['domain'] = [('date_deadline', '>=', start_date),
                            ('date_deadline', '<=', end_date),
                            ('res_model_id', '=', self.cus_res_model_id.id)
                            ]
        return action

#odoo13    @api.multi
    def action_last_week_activity(self):
        action = self.env.ref(
            'schedule_activity_dashboard.custom_action_smart_box'
        ).read()[0]
        today = date.today()
        start_date = today + timedelta(-today.weekday(), weeks=-1)
        end_date = today + timedelta(-today.weekday() - 1)
        action['domain'] = [('date_deadline', '>=', start_date),
                            ('date_deadline', '<=', end_date),
                            ('res_model_id', '=', self.cus_res_model_id.id)
                            ]
        return action

#odoo13    @api.multi
    def action_today_email_activity(self):
        action = self.env.ref(
            'schedule_activity_dashboard.custom_action_smart_box'
        ).read()[0]
        today = date.today()
        action['domain'] = [('activity_type_id', '=', 'Email'),
                            ('date_deadline', '=', today),
                            ('res_model_id', '=', self.cus_res_model_id.id)
                            ]
        return action

#odoo13    @api.multi
    def action_today_phone_activity(self):
        action = self.env.ref(
            'schedule_activity_dashboard.custom_action_smart_box'
        ).read()[0]
        today = date.today()
        action['domain'] = [('activity_type_id', '=', 'Call'),
                            ('date_deadline', '=', today),
                            ('res_model_id', '=', self.cus_res_model_id.id)
                            ]
        return action

#odoo13    @api.multi
    def action_today_meeting_activity(self):
        action = self.env.ref(
            'schedule_activity_dashboard.custom_action_smart_box'
        ).read()[0]
        today = date.today()
        action['domain'] = [('activity_type_id', '=', 'Meeting'),
                            ('date_deadline', '=', today),
                            ('res_model_id', '=', self.cus_res_model_id.id)
                            ]
        return action

#odoo13    @api.multi
    def action_to_do_activity(self):
        action = self.env.ref(
            'schedule_activity_dashboard.custom_action_smart_box'
        ).read()[0]
        today = date.today()
        action['domain'] = [('activity_type_id', '=', 'To Do'),
                            ('date_deadline', '=', today),
                            ('res_model_id', '=', self.cus_res_model_id.id)
                            ]
        return action

#odoo13    @api.multi
    def action_week_mail_activity(self):
        action = self.env.ref(
            'schedule_activity_dashboard.custom_action_smart_box'
        ).read()[0]
        today = date.today()
        start_of_week = datetime.now() - \
            timedelta(days=datetime.now().weekday())
        end_of_week = start_of_week + timedelta(days=6)
        action['domain'] = [('activity_type_id', '=', 'Email'),
                            ('date_deadline', '>=', start_of_week),
                            ('date_deadline', '<=', end_of_week),
                            ('res_model_id', '=', self.cus_res_model_id.id)
                            ]
        return action

#odoo13    @api.multi
    def action_week_phone_activity(self):
        action = self.env.ref(
            'schedule_activity_dashboard.custom_action_smart_box'
        ).read()[0]
        today = date.today()
        start_of_week = datetime.now() - \
            timedelta(days=datetime.now().weekday())
        end_of_week = start_of_week + timedelta(days=6)
        action['domain'] = [('activity_type_id', '=', 'Call'),
                            ('date_deadline', '>=', start_of_week),
                            ('date_deadline', '<=', end_of_week),
                            ('res_model_id', '=', self.cus_res_model_id.id)
                            ]
        return action

#odoo13    @api.multi
    def action_week_meeting_activity(self):
        action = self.env.ref(
            'schedule_activity_dashboard.custom_action_smart_box'
        ).read()[0]
        today = date.today()
        start_of_week = datetime.now() - \
            timedelta(days=datetime.now().weekday())
        end_of_week = start_of_week + timedelta(days=6)
        action['domain'] = [('activity_type_id', '=', 'Meeting'),
                            ('date_deadline', '>=', start_of_week),
                            ('date_deadline', '<=', end_of_week),
                            ('res_model_id', '=', self.cus_res_model_id.id)
                            ]
        return action

#odoo13    @api.multi
    def action_do_meeting_activity(self):
        action = self.env.ref(
            'schedule_activity_dashboard.custom_action_smart_box'
        ).read()[0]
        today = date.today()
        start_of_week = datetime.now() - \
            timedelta(days=datetime.now().weekday())
        end_of_week = start_of_week + timedelta(days=6)
        action['domain'] = [('activity_type_id', '=', 'To Do'),
                            ('date_deadline', '>=', start_of_week),
                            ('date_deadline', '<=', end_of_week),
                            ('res_model_id', '=', self.cus_res_model_id.id)
                            ]
        return action

#odoo13    @api.multi
    def action_past_activity(self):
        action = self.env.ref(
            'schedule_activity_dashboard.custom_action_smart_box'
        ).read()[0]
        today = date.today()
        previous_date = today - timedelta(days=3)
        action['domain'] = [('date_deadline', '=', previous_date),
                            ('res_model_id', '=', self.cus_res_model_id.id)
                            ]
        return action

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
