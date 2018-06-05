# -*- coding: utf-8 -*-


from datetime import datetime, timedelta
from odoo import api, fields, models, _
from odoo.tools import DEFAULT_SERVER_DATE_FORMAT, DEFAULT_SERVER_DATETIME_FORMAT


class DemoCompanyWizard(models.TransientModel):
    _name = 'demo.company.settings'
    _inherit = 'demo.company.settings'


    stay = fields.Boolean('Generate more')


    employee_ids = fields.Many2many(
        comodel_name='hr.employee',
        relation='employee_demo_attendace_generator_rel',
        column1='generator_id', column2='employee_id',
        string='Employees'
    )

    date_start = fields.Date('Start date')
    date_end = fields.Date('End date')

    fixed_start = fields.Boolean('Fixed start time')
    check_in = fields.Float()
    check_in_max = fields.Float()

    fixed_end = fields.Boolean('Fixed end time')
    check_out = fields.Float()
    check_out_max = fields.Float()

    skip_sub = fields.Boolean('Skip saturday')
    skip_ned = fields.Boolean('Skip sunday')

    def clear_all_attendances(self):
        self.env.cr.execute("delete from hr_attendance")


    @api.multi
    def generate_attendance(self):
        att = self.env['hr.attendance']
        start = datetime.strptime(self.date_start, DEFAULT_SERVER_DATE_FORMAT)
        end = datetime.strptime(self.date_end, DEFAULT_SERVER_DATE_FORMAT)

        def add_day(d):
            d += timedelta(days=1)
            return d

        for generator in self:
            for employee in generator.employee_ids:
                estart = start
                while estart != end:
                    if self.skip_sub and estart.weekday() == 5:
                        estart = add_day(estart)
                        continue
                    if self.skip_ned and estart.weekday() == 6:
                        estart = add_day(estart)
                        continue

                    check_in = estart + timedelta(hours=self.check_in)
                    check_out = estart + timedelta(hours=self.check_out)
                    vals = {
                        'employee_id': employee.id,
                        'check_in': check_in,
                        'check_out': check_out
                    }
                    att.create(vals)
                    estart += timedelta(days=1)

