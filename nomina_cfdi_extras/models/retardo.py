# -*- coding: utf-8 -*-
from odoo import models, fields, _, api
import pytz
from .tzlocal import get_localzone
from datetime import datetime, timedelta
from odoo.exceptions import UserError


class RetardoNomina(models.Model):
    _name = 'retardo.nomina'
    _description = 'RetardoNomina'

    name = fields.Char("Name", required=True, copy=False, readonly=True, states={'draft': [('readonly', False)]}, index=True, default=lambda self: _('New'))
    employee_id = fields.Many2one('hr.employee', string='Empleado')
    fecha = fields.Date('Fecha')
    state = fields.Selection([('draft', 'Borrador'), ('done', 'Hecho'), ('cancel', 'Cancelado')], string='State', default='draft')
    company_id = fields.Many2one('res.company', 'Company', required=True, index=True, default=lambda self: self.env.company)
    crear_ausencia = fields.Boolean('Descuento en nómina')
    tiempo = fields.Float('Tiempo retardo (minutos)')

    @api.model
    def init(self):
        company_id = self.env['res.company'].search([])
        for company in company_id:
            retardo_nomina_sequence = self.env['ir.sequence'].search([('code', '=', 'retardo.nomina'), ('company_id', '=', company.id)])
            if not retardo_nomina_sequence:
                retardo_nomina_sequence.create({
                        'name': 'Retardo nomina',
                        'code': 'retardo.nomina',
                        'padding': 4,
                        'company_id': company.id,
                    })

    @api.model
    def create(self, vals):
        if vals.get('name', _('New')) == _('New'):
            if 'company_id' in vals:
                vals['name'] = self.env['ir.sequence'].with_context(force_company=vals['company_id']).next_by_code('retardo.nomina') or _('New')
            else:
                vals['name'] = self.env['ir.sequence'].next_by_code('retardo.nomina') or _('New')
        result = super(RetardoNomina, self).create(vals)
        return result

    
    def action_validar(self):
        if self.crear_ausencia:
           leave_type = None
           leave_type = self.company_id.leave_type_fr or False

           date_from = self.fecha.strftime('%Y-%m-%d') +' 10:00:00'
           date_to = self.fecha.strftime('%Y-%m-%d') +' 10:00:00'
        
           timezone = self._context.get('tz')
           if not timezone:
               timezone = self.env.user.partner_id.tz or 'UTC'
           #timezone = tools.ustr(timezone).encode('utf-8')

           local = pytz.timezone(timezone) #get_localzone()
           naive_from = datetime.strptime (date_from, "%Y-%m-%d %H:%M:%S")
           local_dt_from = local.localize(naive_from, is_dst=None)
           utc_dt_from = local_dt_from.astimezone (pytz.utc)
           date_from = utc_dt_from.strftime ("%Y-%m-%d %H:%M:%S")

           naive_to = datetime.strptime (date_to, "%Y-%m-%d %H:%M:%S") + timedelta(minutes=self.tiempo)
           local_dt_to = local.localize(naive_to, is_dst=None)
           utc_dt_to = local_dt_to.astimezone (pytz.utc)
           date_to = utc_dt_to.strftime ("%Y-%m-%d %H:%M:%S")

           nombre = 'Retardo_' + self.name
           registro_falta = self.env['hr.leave'].search([('name','=', nombre)], limit=1)
           if registro_falta:
              registro_falta.write({'date_from' : date_from,
                      'date_to' : date_to,
                      'employee_id' : self.employee_id.id,
                      'holiday_status_id' : leave_type and leave_type.id,
                      'state': 'validate',
                      })
           else:
              holidays_obj = self.env['hr.leave']
              vals = {'date_from' : date_from,
                  'holiday_status_id' : leave_type and leave_type.id,
                  'employee_id' : self.employee_id.id,
                  'name' : 'Faltas_'+self.name,
                  'date_to' : date_to,
                  'state': 'confirm',}

              holiday = holidays_obj.new(vals)
              holiday._onchange_employee_id()
              holiday._onchange_leave_dates()
              vals.update(holiday._convert_to_write({name: holiday[name] for name in holiday._cache}))
              vals.update({'holiday_status_id' : leave_type and leave_type.id,})
              falta = self.env['hr.leave'].create(vals)
              falta.action_validate()
        self.write({'state':'done'})
        return

    def action_cancelar(self):
        if self.state == 'draft':
            self.write({'state':'cancel'})
        elif self.state != 'draft' and self.crear_ausencia:
           self.write({'state':'cancel'})
           nombre = 'Retardo_' + self.name
           registro_falta = self.env['hr.leave'].search([('name','=', nombre)], limit=1)
           if registro_falta:
              registro_falta.action_refuse()

    def action_draft(self):
        self.write({'state':'draft'})

    def unlink(self):
        raise UserError("Los registros no se pueden borrar, solo cancelar.")

    def action_change_state(self):
        for retardo in self:
            if retardo.state == 'draft':
                retardo.action_validar()
