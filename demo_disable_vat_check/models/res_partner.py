# -*- coding: utf-8 -*-

from odoo import api, models, _


class ResPartner(models.Model):
    _inherit = 'res.partner'

    @api.constrains("vat")
    def check_vat(self):
        if self.env.context.get('company_id'):
            company = self.env['res.company'].browse(self.env.context['company_id'])
        else:
            company = self.env.user.company_id
        res = True
        if company.vat_demo == 'normal':
            return super(ResPartner, self).check_vat()
        elif company.vat_demo == 'country':
            if company.counntry_id and company.country_id.code != self.vat[:2]:
                res = False

        elif company.vat_demo == 'oib':
            vat = self.vat
            vat = vat.upper().replace('HR','')
            if len(vat) != 11:
                res = False

        return res
