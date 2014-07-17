# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from openerp.osv import fields, osv

class task(osv.osv):
    _inherit = 'project.task'
    _columns = {
        'planned_hours': fields.float('Planned Hours', 
            help='Estimated time to do the task, usually set by the project manager when the task is in draft state.',
            track_visibility='onchange'),
        'date_start': fields.date('Start Date',select=True,track_visibility='onchange'),
        'date_end': fields.date('End Date',select=True,track_visibility='onchange'),
        'description': fields.text('Description',select=True,track_visibility='onchange'),
        # 'task_type': fields.selection([('activity', 'Activity'),('feature', 'Feature'),('change', 'Change'),('issue', 'Issue')], 'Type',
        #                                  track_visibility='onchange',
        #                                  help="Indicates the type of task:\n"
        #                                       " * Activity - General activities\n"
        #                                       " * Feature -  New feature request\n"
        #                                       " * Change -  Change request\n"
        #                                       " * Issue -  Bugs/Issues",
        #                                  required=True),
    }

    def msg_pool(self,cr,uid,vals,context=None):
        if not vals.get('planned_hours',True):
            raise osv.except_osv(("Warning!"), ("Planned time should be greater than 0"))
        return True

    def create(self, cr, uid, vals, context=None):
    # Prevent double project creation when 'use_tasks' is checked!
        self.msg_pool(cr,uid,vals,context=None)
        return super(task, self).create(cr, uid, vals, context)

    def write(self, cr, uid, ids, vals, context=None):
    # Prevent double project creation when 'use_tasks' is checked!
        self.msg_pool(cr,uid,vals,context=None)
        return super(task, self).write(cr, uid, ids, vals, context)
        
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
