# -*- coding: utf-8 -*-


from odoo import fields, models


class ResCompany(models.Model):
    _inherit = 'res.company'

    vat_demo = fields.Selection(
        selection=[
            ('normal', 'Normal'),
            ('country', 'Country code'),
            ('oib', '11 digit (w/wo HR)'),
            ('none', 'No check')
        ],
        string='Demo VAT Check', default='normal',
        help="""Normal - normal behaviour, checks AVT number according to country
             Check only country prefix - Demands only country prefix entered on vat, no other check
             11 munbers - Croati aOIB - with or without prefix only check 11 digit structure
             No check - accepts any string value without any checks""")
