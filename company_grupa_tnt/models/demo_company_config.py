# -*- coding: utf-8 -*-

from odoo import api, fields, models, _


class DemoCompanyWizard(models.TransientModel):
    _name = 'demo.company.settings'
    _inherit = 'res.config.settings'


    company_id = fields.Many2one('res.company', string='Company', required=True,
                                 default=lambda self: self.env.user.company_id)

