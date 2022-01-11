# -*- coding:utf-8 -*-

from odoo import fields, models, api

class Ejidos(models.Model):
    _name = "ejidos"

    name = fields.Char("Nombre del Ejido")
    calle = fields.Char("Calle")
    numero = fields.Char("Numero o lote")
    colonia = fields.Char("Colonia")
    cp = fields.Char("Codigo Postal")
    ciudad = fields.Char("Ciudad")
    estado = fields.Char("Estado")
    pais = fields.Char("Pais")
    categoria_id = fields.Many2one(
            comodel_name="ejido.tags"
    )
    acta = fields.Binary("Acta de Asamblea PROCEDE")
    convenio = fields.Binary("Convenio de Compra")
    state = fields.Selection([
                ('draft', 'Borrador'),        
                ('confirm', 'Validado'),
                    
                ], string='Estado', readonly=True, copy=False, index=True, default='draft', compute='status_ejido')
    @api.depends('state')
    def status_ejido(self):
               
            
            if self.acta and self.convenio:
                self.state='confirm'
            else:
                self.state='draft'

                

        