##############################################################################
#
#    OpenERP, Open Source ERP Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).

##############################################################################
{
    'name': 'Purchase_Amendment',
    'version': '0.1',
    'author': 'sengottuvel',
    'category': 'Purchase_Amendment',
    'website': 'http://www.openerp.com',    
    'depends' : ['base', 'product', 'purchase'],
    'data': ['purchase_amendment_view.xml'],
    'auto_install': False,
    'installable': True,
}

