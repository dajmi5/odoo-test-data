# -*- coding: utf-8 -*-


from odoo import fields, models


class ResCompany(models.Model):
    _inherit = 'res.company'

    iban_demo = fields.Selection(
        selection=[
            ('normal', 'Normal'),
            ('country', 'Country code'),
            ('none', 'No check')
        ],
        string='Demo IBAN Check', default='normal',
        help="""Normal - normal behaviour, checks IBAN number according to rules
             Country code - Demands only country prefix entered on IBAN, no other check
             No check - accepts any string value without any checks""")
