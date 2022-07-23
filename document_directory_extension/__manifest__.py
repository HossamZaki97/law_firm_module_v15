# -*- coding: utf-8 -*-

# Part of Probuse Consulting Service Pvt Ltd. See LICENSE file for full copyright and licensing details.

{
    'name': "Attachment/Document Extension with Directory and Numbering",
    'price': 99.0,
    'currency': 'EUR',
    'license': 'Other proprietary',
    'summary': """Attachment/Document Extension with Directory and Numbering""",
    'description': """
Document Extension
Document Extension. This module add directory on ir.attachment model
Attachment/Document Extension with Directory and Numbering
Document Extension
Document Attchment
Attchment
Attachment/Document Extension with Directory and Numbering

This module will add below features to document/attachment module of Odoo.
1. Creation directory/folder by model/object.
2. Every directory/folder having separate sequence numbering for attachments.
3. Security on directory so only specific group can access/create document/attachment inside that directory. (Optional if you do not select group then no security).
4. Directory hierarcy view.
5. Document menu is only avaialble for Document Manager group. (New group has been created for Document Manager).
6. This app is totally dedicated to Document Manager who manage document of ERP.
Available Menus:
document management system
dms
alfresco similar
document number
diretory number
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
document folders
attachment unique number
reference unique number
    """,

    'author': "Probuse Consulting Service Pvt. Ltd.",
    'website': "http://www.probuse.com",
    'support': 'contact@probuse.com',
    'images': ['static/description/img1.jpeg'],
    #'live_test_url': 'https://youtu.be/FHTL19c-dsQ',
    'live_test_url': 'https://youtu.be/kZ4y90KXmWQ',
    'version': '2.11',
    'category' : 'Document Management',
    'depends': [
                #'document',
                'mail',
                ],
    'data':[
        'security/document_security.xml',
        'security/ir.model.access.csv',
        'data/mail_attachment_data.xml',
        'data/directory_sequence.xml',
        'views/document.xml',
        'views/attachment_directory.xml',
    ],
    'installable' : True,
    'application' : False,
    'auto_install' : False,
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
