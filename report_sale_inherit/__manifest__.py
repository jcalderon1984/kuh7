# -*- coding: utf-8 -*-
{
    'name': 'Reporte de cotizacion modificado',
    'summary': 'Cambios en el reporte',
    'description': '''
    * Cambia las 4 decimales a 2 decimales.
    ''',
    "website": "https://www.kuh7.mx",
    'author': 'KUH7 SOLUCIONES S.A. DE C.V.',
    'version': '1.1',
    'category': 'sale',
    'depends': [
        'sale',
    ],
    'data': [
        'views/report_sale_inherit.xml',
    ],
    'installable': True,
    'application': True
}
