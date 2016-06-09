# -*- coding: utf-8 -*-
##############################################################################
#
# This file is part of hr_timesheet_sheet_change_period,
# an Odoo module.
#
# Authors: ACSONE SA/NV (<http://acsone.eu>)
#
# hr_timesheet_sheet_change_period is free software:
# you can redistribute it and/or modify it under the terms of the GNU
# Affero General Public License as published by the Free Software
# Foundation,either version 3 of the License, or (at your option) any
# later version.
#
# hr_timesheet_sheet_change_period is distributed
# in the hope that it will be useful, but WITHOUT ANY WARRANTY; without
# even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR
# PURPOSE. See the GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with hr_timesheet_sheet_change_period.
# If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from openerp import models, fields, api


class hr_sing_out_project(models.TransientModel):

    _inherit = 'hr.sign.out.project'

    task_id = fields.Many2one(
        'project.task',
        string='Task')

    @api.model
    def _write(self, data, emp_id):
        timesheet_id = super(hr_sing_out_project, self)._write(data, emp_id)
        timesheet = self.env['hr.analytic.timesheet'].browse(timesheet_id)
        if data.task_id:
            timesheet.write({'task_id': data.task_id.id})
        return timesheet_id
