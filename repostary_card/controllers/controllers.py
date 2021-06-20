# -*- coding: utf-8 -*-
# from odoo import http


# class RepostaryCard(http.Controller):
#     @http.route('/repostary_card/repostary_card/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/repostary_card/repostary_card/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('repostary_card.listing', {
#             'root': '/repostary_card/repostary_card',
#             'objects': http.request.env['repostary_card.repostary_card'].search([]),
#         })

#     @http.route('/repostary_card/repostary_card/objects/<model("repostary_card.repostary_card"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('repostary_card.object', {
#             'object': obj
#         })
