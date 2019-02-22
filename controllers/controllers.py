# -*- coding: utf-8 -*-
from odoo import http

# class MovimientosAragon(http.Controller):
#     @http.route('/movimientos_aragon/movimientos_aragon/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/movimientos_aragon/movimientos_aragon/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('movimientos_aragon.listing', {
#             'root': '/movimientos_aragon/movimientos_aragon',
#             'objects': http.request.env['movimientos_aragon.movimientos_aragon'].search([]),
#         })

#     @http.route('/movimientos_aragon/movimientos_aragon/objects/<model("movimientos_aragon.movimientos_aragon"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('movimientos_aragon.object', {
#             'object': obj
#         })