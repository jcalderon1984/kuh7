# -*- coding:utf-8 -*-

from odoo import fields, models, api, SUPERUSER_ID
import logging
_logger = logging.getLogger(__name__)
class Ejidos(models.Model):
    _name = "ejidatarios"    
    #_order = "priority desc, id desc"
    _inherit = [ 'image.mixin']
    #_primary_email = 'email_from'

  

    name = fields.Char("Número de lote")

    ejido_id = fields.Many2one(
            comodel_name="ejidos",
            string=('Ejido'), )

    name_id = fields.Many2one(
            comodel_name="res.partner",
            string=('Propietario'),)

    conyugue = fields.Many2one(
            comodel_name="res.partner",
            string=('Esposa(o)'),)

    hijos = fields.Many2many(
            comodel_name="res.partner",
            string=('Hijas(os)'),)

    vende = fields.Selection(
            selection=[('PEND', 'PENDIENTE'),
                       ('SI', 'SI'),
                       ('NO', 'No'),],
            string=('¿Vende?'),)

    propietario = fields.Selection(
            selection=[('PEND', 'PENDIENTE'),
                       ('SI', 'SI'),
                       ('NO', 'No'), ],
            string=('¿Es Propietario?'), )

    vendido = fields.Selection(
            selection=[('PEND', 'PENDIENTE'),
                       ('SI', 'SI'),
                       ('NO', 'No'), ],
            string=('¿Vendió?'), )

    categoria_id = fields.Many2one(
            comodel_name="ejidatarios.tags",
            string=('Categoria'), )

    titular = fields.Many2one(
            comodel_name="res.partner",
            string=('Titular'),)

    concubina = fields.Many2one(
            comodel_name="res.partner",
            string=('Concubino(a)'),)

    ine = fields.Binary(" CREDENCIAL INE")
    derechos = fields.Binary("COPIA CERTIFICADA DE DERECHOS")
    actanac = fields.Binary("ACTA DE NACIMIENTO HIJA(O)")
    contrato = fields.Binary("Contrato")
    state = fields.Selection([
                ('draft', 'Borrador'),        
                ('confirm', 'Validado'),
                    
                ], string='Estado', readonly=True, copy=False, index=True, default='draft', compute='status_ejidatario')
    stage_id = fields.Many2one('etapas.ejido',  string='Etapas', copy=False,  group_expand='_read_group_stage_ejedio_ids')
    
    @api.model
    def _read_group_stage_ejedio_ids(self, stages, domain, order):
        # retrieve team_id from the context and write the domain
        # - ('id', 'in', stages.ids): add columns that should be present
        # - OR ('fold', '=', False): add default columns that are not folded
        # - OR ('team_ids', '=', team_id), ('fold', '=', False) if team_id: add team columns that are not folded
        #team_id = self._context.get('default_team_id')
        team_id = self._context.get('default_team_id')
        if team_id:
            search_domain = ['|', ('id', 'in', stages.ids), '|', ('team_id', '=', False), ('team_id', '=', team_id)]
        else:
            search_domain = ['|', ('id', 'in', stages.ids), ('team_id', '=', False)]
        _logger.error('search_domain: %s', search_domain)
        # perform search
        stage_ids = stages._search(search_domain, order=order, access_rights_uid=SUPERUSER_ID)
        _logger.error('stage_ids: %s', stage_ids)
        return stages.browse(stage_ids)


    @api.depends('state')
    def status_ejidatario(self):
               
            
            if self.ine and self.derechos and self.contrato:
                self.state = 'confirm'
            else:
                self.state = 'draft'

    @api.onchange('name_id')
    def _onchange_conyugue(self):
        if self.name_id == False:
            self.update({
                            'conyugue': False,

                    })
        else:
            return {'domain': {'conyugue': [('parent_id', '=', self.name_id.id)]}}

    @api.onchange('name_id')
    def _onchange_hijos(self):
        if self.name_id == False:
            self.update({
                            'hijos': False,

                    })
        else:
            return {'domain': {'hijos': [('parent_id', '=', self.name_id.id)]}}
    @api.onchange('name_id')
    def _onchange_concubina(self):
        if self.name_id == False:
            self.update({
                            'concubina': False,

                    })
        else:
            return {'domain': {'concubina': [('parent_id', '=', self.name_id.id)]}}