# -*- coding: utf-8 -*-
{
    'name': 'Reporte de cotizacion modificado',
    'summary': 'Cambio en el reporte',
    'description': '''
    * El precio del producto tiene 4 decimales y cambia 2 decimales.
    ''',
    "website": "https://www.kuh7.mx",
    'author': 'KUH7 SOLUCIONES S.A. DE C.V.',
    'version': '1.2',
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
