# -*- coding: utf-8 -*-
{
    'name': "Personalizaciones Kuh7",

    'summary': """
        Manejo de Bases de Datos de Clientes """,

    'description': """
        Personalizaciones para Kuh7 Soluciones SA de CV. "
    """,

    'author': "Kuh7",
    'website': "http://www.Kuh7.mx",

    'category': 'other',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['contacts','base'],

    # always loaded
    'data': [
        'security/kuh7_security_groups.xml',
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/controlbase.xml',
    ],

    'application': True,
    'installable': True,
}
