from odoo import http
from odoo.http import request

class CardRequestControl(http.Controller):
    @http.route('/card/card/show', type="http", auth='public', website=True)
    def showrequester(self, **kw):
        return http.request.render('repostary_card.create_reqests',{})
      
    @http.route('/card/card/create', type="http", auth='public', website=True)
    def create(self, **kw):
        request.env['createwebsitereq'].sudo().create(kw)
        return request.render("repostary_card.confirm_page",{})
    
    @http.route('/card/card/showinfo', type="http", auth='public', website=True)
    def showrequester(self, **kw):
        show = request.env['card'].sudo().search()
        return http.request.render('repostary_card.card_info',{'show':show})
    
    @http.route('/card/card/UpdateRequest', type="http", auth='public', website=True)
    def showrequester(self, **kw):
        updates = request.env['updaterequest'].sudo().search()
        return http.request.render('repostary_card.updates',{'updates':updates})
    
    @http.route('/card/card/UpdateRequest', type="http", auth='public', website=True)
    def showrequester(self, **kw):
        lasts = request.env['updaterequest'].sudo().search()
        return http.request.render('repostary_card.updates',{'lasts':lasts})