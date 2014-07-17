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

from datetime import datetime
from openerp.osv import fields, osv
from openerp import netsvc

#Begin: Holiday Cateogry Class Definition
class hr_holidays_category(osv.osv):
    _name = 'hr.holidays.category'
    _description='Holidays Categories'           
    _columns = {
        'name':fields.char('Name',size=64,help="Name of the Category (Ex: Weekends, Regional Holidays, Bank Holidays etc.,)"),
        }
    
    _defaults = {} 
    
    _constraints = []           

hr_holidays_category()
#End: Holiday Cateogry Class Definition

#Begin: Holiday Class Definition
class hr_holidays(osv.osv):
    _name = 'hr.holidays.extension'
    _description='Holidays Management'
    _order='date'

    # Begin: Get month and year value for the given date
    def get_month_year(self, cr, uid, ids,args,name, context=None):
        res={}
        for record in self.browse(cr, uid, ids):
            if record.date :
                res[record.id] = {'month':0,'year':0}
                temp = datetime.strptime(record.date, "%Y-%m-%d")
                month = temp.strftime("%m")
                year = temp.strftime("%Y")
                res[record.id] ['month']= str(month)
                res[record.id] ['year']= str(year)
                print res
        return res
    # End: Get month and year value for the given date

    _columns = {
        'date':fields.date('Date'),
        'description':fields.char('Description',size=128),
        'category_id': fields.many2one('hr.holidays.category', 'Category'),
        'active': fields.boolean('Active', help="Check this box to indicate that this holiday is active."),
        'month':fields.function(get_month_year,type="char",size=2,string="Month",method=True,store=True,multi="get_value"),
        'year':fields.function(get_month_year,type="char",size=4,string="Year",method=True,store=True,multi="get_value"),
        }
    
    _defaults = {'active':True} 
    
    _constraints = []           

hr_holidays()
#End: Holiday Class Definition

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
