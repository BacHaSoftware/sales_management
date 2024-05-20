# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Sales To Invoices',
    'author': 'Bac Ha Software',
    'website': 'https://bachasoftware.com',
    'maintainer': 'Bac Ha Software',
    'version': '1.0',
    'category': 'Invoice',
    'sequence': 75,
    'summary': 'Manage your BHS sale to invoice',
    'description': "Create and manage your sale to invoice",
    'depends': ['bhs_sales', 'bhs_invoice_report', 'project'],
    'data': [
        'views/account_move_view.xml',
        'views/invoice_report_view.xml'
    ],
    'demo': [],
    "external_dependencies": {},
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3'
}
