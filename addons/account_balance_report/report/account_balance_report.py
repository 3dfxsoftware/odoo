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

import time
from report import report_sxw
from osv import osv
import datetime


class account_balance_report(report_sxw.rml_parse):
    def __init__(self, cr, uid, name, context):
        super(account_balance_report, self).__init__(cr, uid, name, context=context)
        self.total = 0.0
        self.localcontext.update({
            'time': time,
            'get_period': self._get_period,
            'get_period2': self._get_period2,
            'get_partner': self._get_partner,
            'get_lines': self._get_lines,
            'get_open_balance': self._get_open_bal,
            'get_period_balance': self._get_period_bal,
        })

    def _get_period(self, form):
        return form['date_from']

    def _get_period2(self, form):
        return form['date_to']

    def _get_partner(self, form):
        return form['account_id'][1]

    def _get_lines(self, form):

        dt1 = form['date_from'] + ' 00:00:00'
        dt2 = form['date_to'] + ' 23:59:59'
        account_id = form['account_id'][0]
        data = {}
        self.cr.execute("select date,name,debit,credit from account_move_line where date >= %s and date <= %s and account_id = %s"\
                    ,(dt1, dt2, account_id))
        data = self.cr.dictfetchall()
        return data

    def _get_open_bal(self, form):
        acc_fiscal = self.pool.get('account.fiscalyear')
        if form['current_fiscal_year'] == True:
            dt1 = form['date_from'] + ' 23:59:59'
            time = datetime.datetime.strptime(form['date_from'], '%Y-%m-%d').date().strftime("%Y")
            year_search = acc_fiscal.search(self.cr, self.uid, [('name', '=', time)])
            if year_search:
                date = acc_fiscal.browse(self.cr, self.uid, year_search[0]).date_start
            dt2 = date + ' 00:00:00'
            account_id = form['account_id'][0]
            data = {}
            self.cr.execute("select sum(credit) as credit, sum(debit) as debit from account_move_line where date >= %s and date < %s and account_id = %s"\
                    ,(dt2, dt1, account_id))
            data = self.cr.dictfetchall()
            if not data:
                data = [{'credit': 0.00, 'debit': 0.00}]
            return data[0]

        else:

            dt1 = form['date_from'] + ' 00:00:00'
            account_id = form['account_id'][0]
            data = {}
            self.cr.execute("select sum(debit) as debit,sum(credit) as credit from account_move_line where date <= %s and account_id = %s"\
                        ,(dt1, account_id))
            data = self.cr.dictfetchall()
            return data[0]
        for r in data:
            if r['debit'] > 0:
               r['debit'] = r['debit']
            elif r['credit'] > 0:
               r['credit'] = r['credit']
            else:
                r['debit'] = 0.0
                r['credit'] = 0.0

        return data[0]

    def _get_period_bal(self, form):
        dt1 = form['date_from'] + ' 00:00:00'
        # i = int(dt1)
        dt2 = form['date_to'] + ' 23:59:59'

        account_id = form['account_id'][0]
        data = {}
        self.cr.execute("select sum(debit) as debit,sum(credit) as credit from account_move_line where date >= %s and date <= %s and account_id = %s"\
                    ,(dt1,dt2, account_id))
        data = self.cr.dictfetchall()
        for r in data:
            if r['debit'] > 0:
               r['debit'] = r['debit']

            elif r['credit'] > 0:
               r['credit'] = r['credit']
            else:
                r['debit'] = 0.0
                r['credit'] = 0.0

        return data[0]

report_sxw.report_sxw('report.account.balance.report.wizard', 'accounting.balance.report', 'addons/foss_account_balance_report/report/account_balance_report.rml', parser=account_balance_report, header=False)
