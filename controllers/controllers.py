# -*- coding: utf-8 -*-
# from odoo import http


# class Discograficamulti(http.Controller):
#     @http.route('/discograficamulti/discograficamulti/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/discograficamulti/discograficamulti/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('discograficamulti.listing', {
#             'root': '/discograficamulti/discograficamulti',
#             'objects': http.request.env['discograficamulti.discograficamulti'].search([]),
#         })

#     @http.route('/discograficamulti/discograficamulti/objects/<model("discograficamulti.discograficamulti"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('discograficamulti.object', {
#             'object': obj
#         })
