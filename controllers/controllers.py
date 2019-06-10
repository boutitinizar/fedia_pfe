# -*- coding: utf-8 -*-
from odoo import http

# class FediaPfe(http.Controller):
#     @http.route('/fedia_pfe/fedia_pfe/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/fedia_pfe/fedia_pfe/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('fedia_pfe.listing', {
#             'root': '/fedia_pfe/fedia_pfe',
#             'objects': http.request.env['fedia_pfe.fedia_pfe'].search([]),
#         })

#     @http.route('/fedia_pfe/fedia_pfe/objects/<model("fedia_pfe.fedia_pfe"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('fedia_pfe.object', {
#             'object': obj
#         })