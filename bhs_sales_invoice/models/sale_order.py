# -*- coding: utf-8 -*-

from odoo import fields, api, models, _
from odoo.tools import date_utils
import datetime


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def _prepare_invoice(self):
        invoice_vals = super(SaleOrder, self)._prepare_invoice()
        invoice_vals['eom_accumulation'] = self.eom_accumulation
        month = self.eom_accumulation.month
        month = "0%d" % month if month < 10 else str(month)
        invoice_vals['for_month'] = month
        invoice_vals['for_year_number'] = str(self.eom_accumulation.year)

        return invoice_vals

