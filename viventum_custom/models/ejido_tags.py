# -*- coding:utf-8 -*-

from odoo import fields, models, api

class Ejidos_Etiquetas(models.Model):
        _name = "ejido.tags"

        name = fields.Char("Etiqueta")
        color = fields.Char("Color")
