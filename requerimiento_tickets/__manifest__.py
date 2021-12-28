# -*- coding: utf-8 -*-
{
    'name': "Solicitud de requerimiento etapa 1 ",

    'summary': """
        Solicitud de requerimiento etapa 1""",

    'description': """
        Solicitud de requerimiento etapa 1
    """,

    'author': "Kuh7",
    'website': "http://www.Kuh7.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'helpdesk',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['helpdesk','base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/template_layout.xml',
        # 'views/helpdesk_ticket_inherit.xml',
        'views/requirements_ticket_view.xml',
        'views/steps_ticket_view.xml',
        'views/requirements_helpdesk_template_view_pdf.xml',
        'report/requirements_helpdesk_view_report.xml',
        'views/helpdesk_requirements_view.xml',
        'views/menuitens.xml',
        'views/res_groups_view.xml',

        # 'report/report_menu.xml',
        
        #data
        'data/sequence_folio_data.xml',

    ],
    # only loaded in demonstration mode
    'application': True,
    'installable': True,
}
