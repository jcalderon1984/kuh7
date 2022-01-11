# -*- coding:utf-8 -*-

from odoo import fields, models, api


class Etapas(models.Model):
    _name = "etapas.ejido"

    @api.model
    def default_get(self, fields):
        """ Hack :  when going from the pipeline, creating a stage with a sales team in
            context should not create a stage for the current Sales Team only
        """
        ctx = dict(self.env.context)
        if ctx.get('default_team_id') and not ctx.get('crm_team_mono'):
            ctx.pop('default_team_id')
        return super(Etapas, self.with_context(ctx)).default_get(fields)

    name = fields.Char("Nombre de la Etapa")
    team_id = fields.Many2one('crm.team', string='Sales Team', ondelete='set null',
        help='Specific team that uses this stage. Other teams will not be able to see or use this stage.')