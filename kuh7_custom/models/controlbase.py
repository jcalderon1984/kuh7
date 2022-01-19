# -*- coding:utf-8 -*-

from odoo import fields, models, api


class Dbases(models.Model):
    _name = "controldb"
    _inherit = ['image.mixin']

    name = fields.Char("Nombre de la BD")
    name_id_cliente = fields.Many2one(
        comodel_name='res.partner',
        string="Cliente",)

    produccion = fields.Char("Base de Produccion")
    vigprod = fields.Date("Vigencia Produccion")
    usuarios = fields.Integer("Numero de Usuarios")
    user = fields.Many2one(
        comodel_name='res.users',
        string="Responsable",)
    modalidad=fields.Selection(
        selection=[('Online', 'Online'),
                   ('SH', 'SH'),
                   ('OnPremise', 'OnPremise'),]
    )

    pruebas = fields.Char("Base de Pruebas")

    exprueba = fields.Date("Expiracion Pruebas")

    name_id_integrante = fields.Many2many(
        comodel_name='res.users',
        string="user_id",)
    useradmin = fields.Char("Usuario implementación")

    pwdadmin = fields.Char("Password")

    aplicaciones_ids = fields.One2many('aplicaciones', 'controldb_id', string='Aplicaciones')
class aplictions(models.Model):
    _name = 'aplicaciones'

    controldb_id = fields.Many2one('controldb', string="Control")
    module_id  = fields.Many2one('ir.module.module', string='Aplicación')
    name_tec = fields.Char(related='module_id.name', string='Nombre tecnico')
