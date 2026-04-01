# -*- coding: utf-8 -*-

from odoo import fields, api, models, _
import datetime
from odoo.tools.sql import SQL

class AccountInvoiceReport(models.Model):
    _inherit = "account.invoice.report"

    eom_accumulation = fields.Date(string="EOM accumulation", help="End of Month Accumulation.", readonly=True)

    def _select(self):
        return SQL(
            "%s, move.eom_accumulation as eom_accumulation",
            super()._select()
        )

    @api.model
    def read_group(self, domain, fields, groupby, offset=0, limit=None, orderby=False, lazy=True):
        for g in groupby:
            if 'eom_accumulation' in g and self.env.context.get('order_by_eom_accumulation'):
                orderby = g + ' desc'
                break
        res = super(AccountInvoiceReport, self).read_group(domain, fields, groupby, offset=offset, limit=limit,
                                                 orderby=orderby, lazy=lazy)
        return res