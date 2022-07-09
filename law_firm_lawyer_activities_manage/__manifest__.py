# -*- coding: utf-8 -*-

# Part of Probuse Consulting Service Pvt Ltd. See LICENSE file for full copyright and licensing details.

{
    'name' : 'Schedule Activities for Law Firm Users',
    'version' : '1.2.1',
    'price' : 49.0,
    'currency': 'EUR',
    'category': 'Operations/Project',
    'license': 'Other proprietary',
    'live_test_url': 'https://youtu.be/InmW5Pwz7Eo',
    'images': [
        'static/description/image.jpg'
    ],
    'summary' : 'Legal Practitioner with Schedule Activities | Activities for Law Firm Users',
    'description': """
Law Firm Schedule Activities
Legal Practitioner with Schedule Activities
Schedule Activities for Lawyer / Advocate/ Law Firm Users
This app allows you to manage Activities Case Hearnings (Tasks) for law firm practice management systems as shown in below screenshots.
This app adds menus for Activities inside Law Firms apps where users can view activities.
Allow your users (Lawyer/Advocate/Legal User/Officer/Manager) to view and manage schedule activities as shown in below screenshots.
Please note that scheduled activities in open chatter is a feature of odoo standard (out of box feature). Our app allows you to view activities related to users in one place and allows them to search activities and also shows a dashboard for Tasks where you can see your activities quickly.
You can check dependent apps also to get more details about law firm management.
Law
- Activity
- Dashboard
- All Activities
- My Team Activities
- My Activities
- Configuration
- Schedule Activity
    """,
    'author' : 'Probuse Consulting Service Pvt. Ltd.',
    'website' : 'wwww.probuse.com',
    'depends' : [
            'schedule_activity_dashboard',
            'schedule_activity_global',
            'law_firms_advocate_odoo',
        
    ],
    'support': 'contact@probuse.com',
    'data' : [
        'views/menu.xml'
    ],
    'installable' : True,
    'application' : False,
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
