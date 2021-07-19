# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api, _


class AccountMove(models.Model):
    _inherit = "account.move"

    date = fields.Date(string='Date', required=True, index=True, default=fields.Date.context_today)
