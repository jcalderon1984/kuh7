# -*- coding: utf-8 -*-

from odoo import models, fields, api, _, exceptions
import logging
logger = logging.getLogger(__name__)

class RequirementsHelpdesk(models.Model):
    _name = 'requirements.helpdesk'
    _description = 'Solicitud de requerimiento etapa 1'

    partner_id = fields.Many2one('res.partner', string='Cliente')
    name = fields.Char(string='Folio', default=lambda self: self.env['ir.sequence'].next_by_code('requirements.helpdesk'))
    project_id = fields.Many2one('project.project', string='Proyecto')
    modulo = fields.Char(string='Módulo')
    state = fields.Selection([('r', 'Reportado'), ('p', 'Pendiente'),('l','Liberado'),('a','Atrasado'),('u','Urgente')], string='Estado', default='r')
    seccion = fields.Char(string='Proceso')
    fecha_solicitud = fields.Date(string='Fecha de solicitud')
    desarrollador = fields.Many2one('res.users',string='Desarrollador')
    fecha_reporte = fields.Date('Inicio de desarrollo')
    responsable_id = fields.Many2one('res.users', string='Responsable',  default=lambda self: self.env.user)
    fecha_responsable = fields.Date('Fecha Conclusión')
    requeriments_id = fields.Many2one('requeriments.ticket', string='Nombre de módulo')
    motivo = fields.Text(string='Motivo')
    steps_id = fields.One2many('steps.ticket', 'helpdesk_id', string='Pasos')
    # comment_okawa = fields.Text(string='Comentario OKAWA')
    comment_kuh7 = fields.Text(string='Comentario KUH7')
    is_soporte = fields.Boolean(string='Soporte', default=False)
    is_implementador = fields.Boolean(string='Implementador', default=False)
    is_operacion = fields.Boolean(string='Operaciones', default=False)
    is_infraestructura = fields.Boolean(string='Infraestructura', default=False)
    operacion = fields.Boolean(string="Operaciones", default="False")
    developed_implementer = fields.Many2one('res.users', string='Elaboró Implementador')
    reviewed_project_leader = fields.Many2one('res.users', string='Revisó Líder de Proyecto')
    functional_leader_request = fields.Many2one('res.partner', string='Solicitó Líder Funcional')
    project_leader_approved = fields.Many2one('res.partner', string='Aprobó Líder de Proyecto')
    comentarios_dealba= fields.Text(string='COMENTARIOS DEALBA')
    version = fields.Many2one('helpdesk.version', string="Versión")

    def helpdesk_requirements(self):
        # Reporte de ofertas a clientes
        name = 'Solicitud de requerimiento - %s' % (self.name or '',)
        reporte = self.env.ref('requerimiento_tickets.report_requerimiento_tickets_xlsx').sudo().report_file = name
        
        return self.env.ref('requerimiento_tickets.report_requerimiento_tickets_xlsx').report_action(self)

    def print_helpdesk_requirements(self):
        return self.env.ref('requerimiento_tickets.action_helpdesk_template_pdf').report_action(self)

    
    def pendiente(self):
        if self.operacion == True or self.is_infraestructura == True:
            self.state = 'p'
    def liberado(self):
        if self.operacion == True or self.is_infraestructura == True:
            self.state = 'l'
    def atrasado(self):
        if self.operacion == True or self.is_infraestructura == True:
            self.state = 'a'
    def urgente(self):
        if self.operacion == True or self.is_infraestructura == True:
            self.state = 'u'
            
class RequerimentsTicket(models.Model):
    _name = 'requeriments.ticket'
    _description = 'Requerimiento'

    name = fields.Char(string='Título')
    description = fields.Text(string='Descripción')

class StepsTicket(models.Model):
    _name = 'steps.ticket'
    _description = 'Pasos a seguir'

    name = fields.Char('Título')
    description = fields.Text('Descripción')
    helpdesk_id = fields.Many2one('requirements.helpdesk', string='Solicitud de requerimiento')

class HelpDeskVersion(models.Model):
    _name = "helpdesk.version"

    name = fields.Char(string='Versión')