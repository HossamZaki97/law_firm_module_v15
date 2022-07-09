# -*- coding: utf-8 -*-

# Part of Probuse Consulting Service Pvt Ltd. See LICENSE file for full copyright and licensing details.

{
    'name': 'Progress Billing with Law Firm Advocates',
    'version': '2.1.1',
    'price': 9.0,
    'currency': 'EUR',
    'license': 'Other proprietary',
    'summary': """Law Firms Practice with Customer Progress Billing""",
    'description': """
Customer Progress Billing with Law Firm App
Progress Billing to Customer for Law Firm | Legal Practice Advocate
Law Firms Practice with Customer Progress Billing Progress Billing to Customer for Advocate Cases and Hearings
    """,
    'author': 'Probuse Consulting Service Pvt. Ltd.',
    'website': 'http://www.probuse.com',
    'support': 'contact@probuse.com',
    'images': ['static/description/image.jpg'],
    'live_test_url': 'https://youtu.be/v-RhJ7JVJlI',
    'category': 'Accounting/Accounting',
    'depends': [
                'odoo_customer_progress_billing',
                'odoo_job_costing_progress_billing',
                'law_firms_advocate_odoo',
                'law_firms_advocate_costing',
                ],
    'data':[
        'views/project_view.xml',
    ],
    'installable' : True,
    'application' : False,
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
