from openerp.osv import fields, osv
import time
from openerp.tools.translate import _


class accounting_balance_report(osv.osv_memory):
    _name = "accounting.balance.report"
    _description = "Accounting Balance Report"

    def print_report(self, cr, uid, ids, context=None):
        """
             To get the date and print the report
             @param self: The object pointer.
             @param cr: A database cursor
             @param uid: ID of the user currently logged in
             @param context: A standard dictionary
             @return : retrun report
        """
        if context is None:
            context = {}
        datas = {'ids': context.get('active_ids', [])}
        res = self.read(cr, uid, ids, ['date_from', 'date_to', 'account_id', 'current_fiscal_year'], context=context)
        res = res and res[0] or {}
        if res:
            if (res['date_from'] > res['date_to'] or res['date_to'] < ['date_from']):
                raise osv.except_osv(_('UserError !'), _('From date must be set before To date %s') % (str(res['date_to'])))
        datas['form'] = res

        if res.get('id', False):
            datas['ids'] = [res['id']]

        return {
            'type': 'ir.actions.report.xml',
            'report_name': 'account.balance.report.wizard',
            'datas': datas,
        }

    _columns = {
        'account_id': fields.many2one('account.account', 'Account', required=True),
        'date_from': fields.date("From Date"),
        'date_to': fields.date("To Date"),
        'current_fiscal_year': fields.boolean('Current Fiscal Year'),
    }
    _defaults = {
        'date_from': lambda *a: time.strftime('%Y-%m-%d'),
        'date_to': lambda *a: time.strftime('%Y-%m-%d'),
        'current_fiscal_year': True,
    }
accounting_balance_report()
