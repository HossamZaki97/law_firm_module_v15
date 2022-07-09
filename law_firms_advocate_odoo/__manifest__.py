# -*- coding: utf-8 -*-

# Part of Probuse Consulting Service Pvt Ltd. See LICENSE file for full copyright and licensing details.

{
    'name' : 'Law Firms Practice Management',
    'version' : '3.2.2',
    'price' : 99.0,
    'currency': 'EUR',
    'category': 'Operations/Project',
    'license': 'Other proprietary',
    'live_test_url': 'https://youtu.be/6hjXcmylp7s',
    'images': [
        'static/description/img.jpg',
    ],
    'summary' : 'Advocate Cases and Hearings Manage for Law Firm.',
    'description': """
Law Firms Practice Management in Odoo
Advocate Cases and Hearings Manage
Legal Practice Management
Allow your advocate team to manage our cases and case hearings.
Allow your team to manage cases and case hearings.
Configure and manage case type.
Configure and manage FIR police station addresses.
Configure and manage court addresses.
Send the next hearing email reminder notification to your assigned lawyer and customer.
We have extensively used Odoo Project management to build this application so it will be good for you to manage your case as project and case hearing as project task in Odoo.
Allow your customers to view cases and case hearings and related tasks on the website portal my account on your website if those are shared with them.
For more details please check below screenshots and watch the video.
    """,
    'author' : 'Probuse Consulting Service Pvt. Ltd.',
    'website' : 'wwww.probuse.com',
    'depends' : [
        'project',
        'hr',
        'base',
        'sale_timesheet'
    ],
    'support': 'contact@probuse.com',
    'data' : [
        'security/ir.model.access.csv',
        'data/hearing_notification_cron.xml',
        'data/hearing_notification_mail.xml',
        'views/project_view.xml',
        'views/case_type_view.xml',
        'views/fir_police_station_view.xml',
        'views/case_court_view.xml',
        'views/employee_view.xml',
        'views/res_partner_view.xml',
        'views/template.xml',
        'report/project_report_view.xml',
        'views/menus.xml'
    ],
    'installable' : True,
    'application' : False,
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
