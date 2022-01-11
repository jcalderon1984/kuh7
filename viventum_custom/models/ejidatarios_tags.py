# -*- coding:utf-8 -*-

from odoo import fields, models, api

class Ejidatarios_Tags(models.Model):
        _name = "ejidatarios.tags"

        name = fields.Char("Etiqueta")
        color =fields.Char("color")
