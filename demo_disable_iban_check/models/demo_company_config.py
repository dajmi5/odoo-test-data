# -*- coding: utf-8 -*-

from odoo import api, fields, models, _


class DemoCompanyWizard(models.TransientModel):
    _name = 'demo.company.settings'
    _inherit = 'demo.company.settings'


    iban_demo = fields.Selection(related='company_id.vat_demo')

