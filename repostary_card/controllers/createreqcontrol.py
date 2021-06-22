from odoo import http
from odoo.http import request

class CardRequestControl(http.Controller):
    @http.route('/card/card/show', type="http", auth='public', website=True)
    def showrequester(self, **kw):
        return http.request.render('repostary_card.create_reqests',{})
      
    @http.route('/card/card/create', type="http", auth='public', website=True)
    def create(self, **kw):
        request.env['createrequest'].sudo().create(kw)
        return request.render("repostary_card.requestthank",{})