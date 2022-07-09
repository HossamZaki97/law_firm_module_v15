# -*- coding: utf-8 -*-

# Part of Probuse Consulting Service Pvt Ltd. See LICENSE file for full copyright and licensing details.

{
    'name': "Bundle of Law Firm Lawyer Related Apps",
    'version': '1.2.2',
    'price': 1.0,
    'currency': 'EUR',
    'category' : 'Services/Project',
    'license': 'Other proprietary',
    'summary': """This module contains bundle of Law Firm Lawyer Related Apps/Modules.""",
    'description': """
Law Firm Lawyer Related apps
    """,
    'author': "Probuse Consulting Service Pvt. Ltd.",
    'website': "http://www.probuse.com",
    'support': 'contact@probuse.com',
    'images': ['static/description/lbm.jpg'],
    'depends': [
        'law_firms_advocate_odoo',
        'law_firms_advocate_documents',
        'law_firms_advocate_costing',
        'law_firm_lawyer_activities_manage',
        'law_firm_progress_billing',
    ],
    'data':[
        
    ],
    'installable' : True,
    'application' : False,
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
