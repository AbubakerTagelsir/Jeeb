# -*- coding: utf-8 -*-
from odoo import http

# class Jeeb(http.Controller):
#     @http.route('/jeeb/jeeb/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/jeeb/jeeb/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('jeeb.listing', {
#             'root': '/jeeb/jeeb',
#             'objects': http.request.env['jeeb.jeeb'].search([]),
#         })

#     @http.route('/jeeb/jeeb/objects/<model("jeeb.jeeb"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('jeeb.object', {
#             'object': obj
#         })