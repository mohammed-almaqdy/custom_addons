 from odoo import http
from odoo.http import request

class CardRequest(http.Controller):
    @http.route('/card/card/show', auth='public', website=True)
    def showrequester(self, **kw):
        return http.request.render('academy.index')
      
    @http.route('/card/card/create', auth='public', website=True)
    def create(self, **kw):
        request.env[].sudo().create(kw)
        return request.render("")
        