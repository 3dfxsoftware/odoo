# -*- coding: utf-8 -*-
##############################################################################
#
#    Author: Guewen Baconnier
#    Copyright 2010-2012 Camptocamp SA
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
    'name': 'Sales BoMs Split',
    'version': '1.0.1',
    'category': 'Generic Modules/Sales & Purchases',
    'description': """
     This module splits the products into the related packing according to their
     Bill of Materials when validating a sale order.

     BoM example structure:

     Product A (fantom)
        Product B (normal)
            Product B1 (normal)
            Product B2 (normal)
        Product C (fantom)
            Product C1 (normal)
            Product C2 (normal)

     With this module, a sale order of Product A will result in a packing of :

     Product B
     Product C1
     Product C2

     Without this module, it would result in a packing with :

     Product A

    """,
    'author': 'Camptocamp',
    'website': 'http://www.camptocamp.com',
    'depends': ['sale', 'bom_split'],
    'data': [],
    'demo': [],
    'test': ['tests/test_sale_bom_split.yml',
             ],
    'installable': True,
    'auto_install': False,
}

