# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2013 IMSAR
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

{
'name': "IMSAR Rollup",
'version': "1.0",
'depends': [
    "asset",
    "mro",
    "smile_decimal_precision",
    "account_accountant",
    "account_budget",
    "audittrail",
    "stock",
    "project",
    "board",
    "hr_timesheet_sheet",
    "hr_expense",
    "mrp",
    "mrp_jit",
    "mrp_operations",
    "crm",
    "sale_mrp",
    "sale_stock",
    "stock",
    "account_cancel",
    "account_analytic_analysis",
    "product_fifo_lifo",
    "product_fifo_lifo_anglo_saxon",
    "web_printscreen_zb",
    "ui_techmenu",
    ],
'author': "Ben Olsen",
'description': "Collects the required modules for IMSAR's OpenERP install",
'category': "Uncategorized",
'data': [],
'installable': True,
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
