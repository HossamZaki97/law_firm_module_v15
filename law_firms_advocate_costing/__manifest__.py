# -*- coding: utf-8 -*-

# Part of Probuse Consulting Service Pvt Ltd.
#See LICENSE file for full copyright and licensing details.

{
    'name': "Law Firm Project Job Costing",
    'version': '1.2.2',
    'category': 'Operations/Project',
    'license': 'Other proprietary',
    'price': 39.0,
    'currency': 'EUR',
    'summary':  """
        Job Cost Sheet for Law Firms Advocate Project / Cases
    """,
    'description': """
Job Cost Sheet for Law Firms Advocate Project / Cases
Costing for Material / Labour / Overheads for Law Firms Project
Project Law Firms Cases Integrate with Job Cost Sheet
Legal Practice Management with Job Costing of Project
Allow you to set material, labour and overheads items with quantity on Project / Case form and using it allow you to create a new job cost sheet or edit existing job cost sheet for that project.
You can specify materials which are going to be consumed for that Project / Case, labour going to work on that request and overheads going to occur for that Law Firms Advocate Project.
System will allow you to choose whether you want to create a new cost sheet or you want to append lines in an existing job cost sheet.
Using this app you can plan your costing for a project of cases. And you will get an idea about plan cost and you can see actual cost on the job cost sheet form.
    """,
    'author': 'Probuse Consulting Service Pvt. Ltd.',
    'website': 'www.probuse.com',
    'support': 'contact@probuse.com',
   'images': ['static/description/img.jpg'],
   'live_test_url': 'https://youtu.be/NCYMnoRXR5w',
    'depends': [
                'odoo_job_costing_management',
                'law_firms_advocate_odoo',
                ],
    'data': [
        'security/ir.model.access.csv',
        'wizard/law_request_job_costsheet_view.xml',
        'views/project_project_view.xml',
        'views/job_costing_view.xml',
    ],
    'installable': True,
    'application': False,
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
