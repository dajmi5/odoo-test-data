# -*- coding: utf-8 -*-

import re

from odoo import api, models, _
from odoo.exceptions import UserError, ValidationError


class ResPartnerBank(models.Model):
    _inherit = "res.partner.bank"


    @api.one
    @api.constrains('acc_number')
    def _check_iban(self):
        if self.company_id.iban_demo == 'none':
            return True
        elif self.company_id.ibn_demo == 'country':
            if not self.partner_id.country_id:
                raise
            else:
                if self.partner_id.country_id.code != self.acc_number[:2]:
                    raise
        else:
            super(ResPartnerBank, self)._check_iban()


#
