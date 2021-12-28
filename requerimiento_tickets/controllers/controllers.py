# -*- coding: utf-8 -*-
# from odoo import http


# class RequiremientoTickets(http.Controller):
#     @http.route('/requiremiento_tickets/requiremiento_tickets/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/requiremiento_tickets/requiremiento_tickets/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('requiremiento_tickets.listing', {
#             'root': '/requiremiento_tickets/requiremiento_tickets',
#             'objects': http.request.env['requiremiento_tickets.requiremiento_tickets'].search([]),
#         })

#     @http.route('/requiremiento_tickets/requiremiento_tickets/objects/<model("requiremiento_tickets.requiremiento_tickets"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('requiremiento_tickets.object', {
#             'object': obj
#         })
