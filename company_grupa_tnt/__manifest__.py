# -*- coding: utf-8 -*
# © 2016-2018 Davor Bojkić - Bole <bole@dajmi5.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "GRUPA TNT",
    "summary": "DEMO Comapny setup",
    "category": "Test / Demo",
    "images": [],
    "version": "10.0.1.0.0",
    "application": True,

    "author": "DAJ MI 5!",
    "licence": "LGPL-3",

    "depends": [
        # like to have it installed
        # not realy a dependency
         "disable_odoo_online",
         "base_technical_features",
         'web_environment_ribbon',
    ],
    "data": [
        "data/01_res_company.xml",
        "data/02_res_partner_data_af.xml",
        "data/03_res_users_data.xml",
        #"data/update_users_passwords.yml", use carefuly!!!
        "views/demo_company_config_view.xml",
    ],
    "qweb": [],

    "auto_install": False,
    "installable": True,
}

