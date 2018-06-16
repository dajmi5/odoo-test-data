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
            # no check
            return True
        elif self.company_id.iban_demo == 'country':
            if not self.partner_id.country_id:
                raise ValidationError(_("You need to set country on employee home address"))
            else:
                if self.partner_id.country_id.code != self.acc_number[:2]:
                    raise ValidationError(_("Employe country is diffrent from IBAN acc country code!"))
        else:
            super(ResPartnerBank, self)._check_iban()


#
