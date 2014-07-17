# -*- coding: utf-8 -*-


import openerp
import openerp.modules.registry
from openerp.tools.translate import _
from openerp.tools import config
import os
from openerp.addons.web import http
openerpweb = http


class Web_Calculator(openerpweb.Controller):
    _cp_path = '/web/calculator'

    @openerpweb.httprequest
    def path(self, req):
        print config,'CPOMFIGGGGGGGGGGG'
        addons_path = openerpweb.addons_manifest['web_calculator']['addons_path']
        f_name = os.path.join("/web_calculator", "static/src/calculator/calculator.html")
        print str(f_name),'FNAME'
        return str(f_name)


# vim:expandtab:tabstop=4:softtabstop=4:shiftwidth=4:
