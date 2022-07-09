# -*- coding: utf-8 -*-

# Part of Probuse Consulting Service Pvt Ltd. See LICENSE file for full copyright and licensing details.

{
    'name': 'Document Management System for Law Firm App',
    'version': '1.2.1',
    'price': 49.0,
    'category' : 'Projects/Projects',
    'depends': [
        'law_firms_advocate_costing',
        'job_costing_contracting_document',
    ],
    'license': 'Other proprietary',
    'currency': 'EUR',
    'summary': """Firm Practice Management with Document Management System (DMS)""",
    'description': """
Document Management System for Law Firm App
Firm Practice Management with Document Management System (DMS)
Legal Practice Management with Documents Feature
This app allows you to manage documents on Cases (Project) and Hearnings (Tasks) for law firm practice management systems as shown in below screenshots.
This app adds menus for Documents and Directories inside Law Firms apps.
Allow your Law Firms Practice team to configure your directory and document tags and link it with document and directory forms.
Allow your Law Firms team to see all documents related to Law Firms cases and hearings (tasks).
You can get more details for all features of the document and directory by going into the dependency apps index.
Law
- Documents
- Directories
- Parent Directories
- Directories
- All Documents
- My Documents
- Configuration
- Documents
- Document Tags
- Directory Tags
""",
    'author': 'Probuse Consulting Service Pvt. Ltd.',
    'website': 'http://www.probuse.com',
    'support': 'contact@probuse.com',
    'images': ['static/description/image.jpg'],
    'live_test_url': 'https://youtu.be/_dKSYcG5w0s', 
    'data':[
        'views/menu.xml',
        'views/project_view.xml',
    ],
    'installable' : True,
    'application' : False,
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
