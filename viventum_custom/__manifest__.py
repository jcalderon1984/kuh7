# -*- coding: utf-8 -*-
{
    'name': "Personalizaciones Viventum",

    'summary': """
        Personalizaciones para Grupo Inmobiliario y Desarrollador Viventum""",

    'description': """
        Personalizaciones para Grupo Inmobiliario y Desarrollador Viventum"
    """,

    'author': "Kuh7",
    'website': "http://www.Kuh7.mx",

    'category': 'other',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['contacts','base'],

    # always loaded
    'data': [
        'security/viventum_security_groups.xml',
        'security/ir.model.access.csv',
        'views/menu_config.xml',
        'views/etapas.xml',
        'views/ejidatarios_tags.xml',
        'views/ejido_tags.xml',
        'views/ejidos.xml',
        'views/ejidatarios.xml',

    ],

    'application': True,
    'installable': True,
}
