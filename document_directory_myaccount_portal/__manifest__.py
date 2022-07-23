# -*- coding: utf-8 -*-

# Part of Probuse Consulting Service Pvt Ltd. See LICENSE file for full copyright and licensing details.
{
    'name': 'Document Management System - Customer Portal',
    'price': 99.0,
    'depends': ['document_directory_extension', 'document_directory_extension_security', 'portal', 'website'],
    'category': 'Document Management',
    'summary': 'This app allow your customer to download documents which have been shared with them.',
    'author': 'Probuse Consulting Service Pvt. Ltd.',
    'website': 'https://www.probuse.com',
    'currency': 'EUR',
    'license': 'Other proprietary',
    'version': '3.17',
    'description': """
This module will add features to portal user download a document/attachment in website throw.

Document Extension
Document Extension. This module add directory on ir.attachment model
Attachment/Document Extension with Directory and Numbering
Document Extension
Document Attachment
Attachment
Attachment/Document Extension with Directory and Numbering
This module will add below features to document/attachment module of Odoo.
1. Creation directory/folder by model/object.
2. Every directory/folder having separate sequence numbering for attachments.
3. Security on directory so only specific group can access/create document/attachment inside that directory. (Optional if you do not select group then no security).
4. Directory hiearchy view.
5. Document menu is only available for Document Manager group. (New group has been created for Document Manager).
6. This app is totally dedicated to Document Manager who manage document of ERP.
Available Menus:
document management system
my documents
document tags
directory tags
dms
alfresco similar
document number
directory number
file number
file sequence
document search
file store
filestore
dms
document management system
dms
Document
Document/Directories
Document/Directories/Directories
Document/Directories/Directories Structure
Document/Documents
Document/Documents/Documents
Directory Form View
document number
document sequence
document sequence
document numbering
document directory
document folder
folder
directory
* INHERIT Ir attachment.form (form)
* INHERIT Ir attachment.search (search)
* INHERIT Ir attachment.tree (tree)
document.directory form (form)
document.directory search (search)
document.directory tree (tree)
document.directory.hierarchy (tree)
attachment number
attach number
document attach number
document numbering
document number
number attachment
odoo document attachment number
filestore
file store
file number
files number
folder
full dms
dms
tags document
document tags
document number
document folders
attachment unique number
reference unique number

customer portal
customer portal document management
document portal
dms portal
customer dms portal
share customer document
customer share document
customer document share
customer attachment share
website portal share document
""",
    'author': "Probuse Consulting Service Pvt. Ltd.",
    'website': "http://www.probuse.com",
    'support': 'contact@probuse.com',
    'images': ['static/description/img1.jpg'],
    #'live_test_url': 'https://youtu.be/724k9z6BbGc',
    'live_test_url': 'https://youtu.be/8fxbDzrPz0Y',
    'data': [
        'data/data.xml',
        'views/my_document_portal_templates.xml',
        'views/attachment_directory.xml',
    ],
    'installable': True,
    'auto_install': False,
    'assets': {
        'web.assets_frontend': [
            'document_directory_myaccount_portal/static/src/css/website_portal_templates.css',
            # 'document_directory_myaccount_portal/static/src/js/website_portal_templet.js',
        ],
    },
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
