# -*- coding: utf-8 -*-
{
    'name': 'KUH7 - Complemento Contabilidad',
    'summary': 'Modificar campo de fecha contable',
    'description': '''
    * Hacer visible y editable campo de fecha contable
    ''',
    "website": "https://www.kuh7.mx",
    'author': 'Kuh7 Soluciones S.A. de C.V.',
    'version': '1.0',
    'category': 'account',
    'depends': [
        'account',
    ],
    'data': [
        'views/account_move_view.xml'
    ],
    'installable': True,
    'application': False
}