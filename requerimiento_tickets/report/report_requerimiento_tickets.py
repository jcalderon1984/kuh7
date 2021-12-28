import base64
import io
from datetime import datetime

from odoo import models
from xlsxwriter.utility import xl_rowcol_to_cell, xl_range
import logging
logger = logging.getLogger(__name__)

class ReporteSolicitudRequerimeinto (models.AbstractModel):
    _name = 'report.report_solicitud_requerimeinto'
    _inherit = 'report.report_xlsx.abstract'
    _description = 'Reporte de solicitud de requerimiento'


    def generate_xlsx_report(self, workbook, data, objs):
        print(data['data'])
        cadena1 = data['data'].split(",")
        cadena2 = cadena1[0].split("/")
        cadena_fin = cadena2[4].split("\"")
        id_soli = cadena_fin[0]
        print('Formacion', id_soli)

        objs = self.env['requirements.helpdesk'].search([('id', '=', int(id_soli))])
        print(objs)
        format1 = workbook.add_format({'font_size': 14, 'font_name': 'Arial', 'align': 'vcenter', 'bold': True})
        sheet = workbook.add_worksheet('ANEXO 1 EXP.')
        # sheet.write(2, 2, 'name', format1)

        # Formato de las celdas
        #
        # celdas JUSTIFY
        cell_format_justify = workbook.add_format({'align': 'justify'})
        cell_format_justify.set_text_wrap()
        cell_format_justify.set_border(2)
        cell_format_justify.set_font_name('Arial')
        cell_format_justify.set_font_size(10)
        #
        cell_format = workbook.add_format({'align': 'center'})
        cell_format.set_text_wrap()
        cell_format.set_border(2)
        cell_format.set_font_name('Arial')
        cell_format.set_font_size(10)
        #
        cell_format_bold = workbook.add_format({'align': 'left', 'bold': True})
        cell_format_bold.set_text_wrap()
        cell_format_bold.set_border(2)
        cell_format_bold.set_font_name('Arial')
        cell_format_bold.set_font_size(10)
        cell_format_bold.set_bg_color('#c901ff')

        cell_format_bold_left = workbook.add_format({'align': 'left', 'bold': True})
        cell_format_bold_left.set_text_wrap()
        cell_format_bold_left.set_border(2)
        cell_format_bold_left.set_font_name('Arial')
        cell_format_bold_left.set_font_size(10)

        cell_format_left = workbook.add_format({'align': 'left'})
        cell_format_left.set_text_wrap()
        cell_format_left.set_border(2)
        cell_format_left.set_font_name('Arial')
        cell_format_left.set_font_size(10)

        cell_format_bold_left_border = workbook.add_format({'align': 'left', 'bold': True})
        cell_format_bold_left_border.set_text_wrap()
        cell_format_bold_left_border.set_font_name('Arial')
        cell_format_bold_left_border.set_font_size(10)

        cell_format_bold_color = workbook.add_format({'align': 'center', 'bold': True})
        cell_format_bold_color.set_text_wrap()
        cell_format_bold_color.set_border(2)
        cell_format_bold_color.set_bg_color('yellow')
        cell_format_bold_color.set_font_name('Arial')
        cell_format_bold_color.set_font_size(10)

        cell_border = workbook.add_format()
        cell_border.set_border(2)
        cell_border.set_font_name('Arial')
        cell_border.set_font_size(10)
        sheet.set_row(1,50)
        cell_image1 = xl_range(0, 1, 0, 1)
        user = user = self.env.user
        logo = user.company_id.logo
        buf_image = io.BytesIO(base64.b64decode(logo))
        sheet.insert_image(cell_image1, "any_name.png", {'image_data': buf_image, 'x_scale': 0.65, 'y_scale': 0.65})

        sheet.merge_range(0, 0, 3, 11, '', cell_format_bold)
        sheet.merge_range(0, 12, 3, 23, '', cell_format_bold)
        sheet.merge_range(0, 24, 3, 35, '', cell_format_bold)
        sheet.merge_range(0, 36, 3, 47, '', cell_format_bold)
        row = 0
        col = 0
        sheet.merge_range(row + 5, col, row + 5, col + 1, 'CLIENTE',cell_format_bold)
        sheet.merge_range(row+5, col+2, row+5, col+5, objs.partner_id.name,cell_format_left)
        sheet.merge_range(row+6, col, row+6, col+1, 'MÓDULO', cell_format_bold)
        sheet.merge_range(row+6, col+2, row+6, col+5, objs.modulo, cell_format_left)
        sheet.merge_range(row+7, col, row+7, col + 1,'FECHA SOLICITUD',cell_format_bold)
        sheet.merge_range(row+7, col+2, row+7, col+5,str(objs.fecha_solicitud),cell_format_left)

        sheet.merge_range(row + 5, col + 7, row + 5, col + 8, 'FOLIO', cell_format_bold)
        sheet.merge_range(row + 5, col + 9, row + 5, col + 11, objs.name, cell_format_left)
        sheet.merge_range(row+6, col + 7, row+6, col+8, 'SECCIÓN', cell_format_bold)
        sheet.merge_range(row+6, col + 9, row+6, col+11, objs.seccion, cell_format_left)
        sheet.merge_range(row + 7, col + 7, row + 7, col + 8, 'ESTATUS', cell_format_bold)
        if objs.state == 'r':
            sheet.merge_range(row + 7, col + 9, row + 7, col + 11, 'REPORTADO', cell_format_left)
        elif objs.state == 'p':
            sheet.merge_range(row + 7, col + 9, row + 7, col + 11, 'PENDIENTE', cell_format_left)
        elif objs.state == 'l':
            sheet.merge_range(row + 7, col + 9, row + 7, col + 11, 'LIBERADO', cell_format_left)
        elif objs.state == 'a':
            sheet.merge_range(row + 7, col + 9, row + 7, col + 11, 'ATRASADO', cell_format_left)
        else:
            sheet.merge_range(row + 7, col + 9, row + 7, col + 11, 'URGENTE', cell_format_left)

        sheet.merge_range(row+9, col,row+9, col+5, 'IMPLEMENTACIÓN', cell_format)
        sheet.merge_range(row+9, col+7,row+9, col+11, 'DESARROLLO', cell_format)
        sheet.merge_range(row+10, col, row+10, col+1, 'REPORTA', cell_format_bold)
        sheet.merge_range(row+10, col+2, row+10, col+5, objs.desarrollador, cell_format_left)
        sheet.merge_range(row+10, col+7, row+10, col+8, 'RESPONSABLE', cell_format_bold)
        sheet.merge_range(row+10, col+9, row+10, col+11, objs.responsable_id.name, cell_format_left)
        sheet.merge_range(row + 11, col, row + 11, col + 1, 'FECHA', cell_format_bold)
        sheet.merge_range(row + 11, col + 2, row + 11, col + 5, str(objs.fecha_reporte), cell_format_left)
        sheet.merge_range(row + 11, col + 7, row + 11, col + 8, 'FECHA CONCLUSIÓN', cell_format_bold)
        sheet.merge_range(row + 11, col + 9, row + 11, col + 11, str(objs.fecha_responsable), cell_format_left)
        sheet.merge_range(row+13, col, row+13, col+11, 'REQUERIMIENTO:' + str(objs.requeriments_id.name), cell_format_bold)
        sheet.merge_range(row+14, col, row+16, col+11, str(objs.requeriments_id.description),cell_format_left)
        sheet.merge_range(row + 18, col, row + 18, col + 11, 'MOTIVO:',cell_format_bold)
        sheet.merge_range(row + 19, col, row + 22, col + 11, str(objs.motivo), cell_format_left)

        sheet.merge_range(row + 24, col, row + 24, col + 11, 'PASOS A SEGUIR:', cell_format_bold)
        row = 25
        col = 0
        item = 0
        total = 0
        for pas in objs.steps_id:
            total += 1
        for pa in objs.steps_id:
            print(pa)

            item += 1
            if item <= (total/2):
                sheet.merge_range(row, col, row, col+6, str(item) + '-' + str(pa.name), cell_format_left)
            elif item > (total/2):
                sheet.merge_range(row, col+7, row, col + 11, str(item) + '-' + str(pa.name), cell_format_left)
            # row += 1
        row+=1
        print('mira',row)
        sheet.merge_range(row, col, row, col+11, 'COMENTARIO OKAWA', cell_format_bold)
        sheet.merge_range(row+1, col, row+3, col+11, '', cell_format_left)

        sheet.merge_range(row+4, col, row+4, col + 11, 'COMENTARIO OKAWA', cell_format_bold)
        sheet.merge_range(row + 5, col, row + 7, col + 11, objs.comment_kuh7, cell_format_left)

        #aqui va el pie de firma

        sheet.merge_range(row+9, col,row+9, col+7, 'FIRMAS DE KUH7:',cell_format_bold)
        sheet.merge_range(row+9, col+8,row+9, col+11, 'FIRMAS DE CONCLUSIÓN OKAWA:',cell_format_bold)
        sheet.merge_range(row+10, col, row+11, col+1, '',cell_format_bold_left)
        sheet.merge_range(row+10, col+2, row+11, col+3, '',cell_format_bold_left)
        sheet.merge_range(row+10, col+4, row+11, col+5, '',cell_format_bold_left)
        sheet.merge_range(row+10, col+6, row+11, col+7, '',cell_format_bold_left)
        sheet.merge_range(row+10, col+8, row+11, col+9, '', cell_format_bold_left)
        sheet.merge_range(row+10, col+10, row+11, col+11, '', cell_format_bold_left)
        sheet.merge_range(row + 12, col, row+12, col + 1, 'Implementador', cell_format_bold_left)
        sheet.merge_range(row + 12, col + 2, row+12, col + 3, 'Líder de Proyecto', cell_format_bold_left)
        sheet.merge_range(row + 12, col + 4, row+12, col + 5, 'Líder de Desarrollo', cell_format_bold_left)
        sheet.merge_range(row + 12, col + 6, row+12, col + 7, 'Desarrollador', cell_format_bold_left)
        sheet.merge_range(row + 12, col + 8, row+12, col + 9, 'Líder Funcional', cell_format_bold_left)
        sheet.merge_range(row + 12, col + 10, row+12, col + 11, 'Líder de Proyecto', cell_format_bold_left)
        sheet.merge_range(row + 13, col, row + 13, col+1, '', cell_format_bold_left)
        sheet.merge_range(row + 13, col+2, row + 13, col+3, '', cell_format_bold_left)
        sheet.merge_range(row + 13, col+4, row + 13, col+5, '', cell_format_bold_left)
        sheet.merge_range(row + 13, col+6, row + 13, col+7, '', cell_format_bold_left)
        sheet.merge_range(row + 13, col+8, row + 13, col+9, '', cell_format_bold_left)
        sheet.merge_range(row + 13, col+10, row + 13, col+11, '', cell_format_bold_left)
        sheet.merge_range(row + 14, col, row + 14, col + 1, '', cell_format_bold_left)
        sheet.merge_range(row + 14, col + 2, row + 14, col + 3, '', cell_format_bold_left)
        sheet.merge_range(row + 14, col + 4, row + 14, col + 5, '', cell_format_bold_left)
        sheet.merge_range(row + 14, col + 6, row + 14, col + 7, '', cell_format_bold_left)
        sheet.merge_range(row + 14, col + 8, row + 14, col + 9, '', cell_format_bold_left)
        sheet.merge_range(row + 14, col + 10, row + 14, col + 11, '', cell_format_bold_left)

        sheet.merge_range(5, col+12, 5, col+23, 'PASO 1', cell_format_bold)
        sheet.merge_range(6, col+12, 21, col+23, '', cell_format_bold_left)
        sheet.merge_range(22, col+12, 22, col+23, '', cell_format_bold_left)
        sheet.merge_range(24, col+12, 24, col+23, 'PASO 2', cell_format_bold)
        sheet.merge_range(25, col+12, 42, col+23, '', cell_format_bold_left)
        sheet.merge_range(43, col+12, 43, col+23, '', cell_format_bold_left)
        sheet.merge_range(5, col+24, 5, col+35, 'PASO 3', cell_format_bold)
        sheet.merge_range(6, col+24, 21, col+35, '', cell_format_bold_left)
        sheet.merge_range(22, col+24, 22, col+35, '', cell_format_bold_left)
        sheet.merge_range(24, col+24, 24, col+35, 'PASO 4', cell_format_bold)
        sheet.merge_range(25, col+12, 42, col+35, '', cell_format_bold_left)
        sheet.merge_range(43, col+12, 43, col+35, '', cell_format_bold_left)
        sheet.merge_range(5, col+36, 5, col+47, 'PASO 5', cell_format_bold)
        sheet.merge_range(6, col+36, 21, col+47, '', cell_format_bold_left)
        sheet.merge_range(22, col+36, 22, col+47, '', cell_format_bold_left)
        sheet.merge_range(24, col+36, 24, col+47, 'PASO 6', cell_format_bold)
        sheet.merge_range(25, col+36, 42, col+47, '', cell_format_bold_left)
        sheet.merge_range(43, col+36, 43, col+47, '', cell_format_bold_left)
        sheet.merge_range(50, 0, 53, 11, '', cell_format_bold)
        sheet.merge_range(50, 12, 53, 23, '', cell_format_bold)
        sheet.merge_range(50, 24, 53, 35, '', cell_format_bold)
        sheet.merge_range(50, 36, 53, 47, '', cell_format_bold)
        workbook.close()
        logger.error('workbook: %s', workbook)