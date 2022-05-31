# -*- coding: utf-8 -*-

{
    'name': 'Nomina CFDI Extras',
    'summary': '',
    'description': '''
Create new module for Odoo 13 called nomina_cfdi_extras. 
This new module will create 2 new models: incidencias and incapacidades, they will have a tree view and will be located on Employees view. For both create sequential numbers for each register. Will have only 2 states: draft and done.
    ''',
    'author': 'IT Admin',
    'version': '13.08',
    'category': 'Employees',
    'depends': [
        'hr','nomina_cfdi',
        'report_xlsx', 'om_hr_payroll', #"om_hr_payroll_account",
    ],
    'data': [
        'data/hr_data.xml',
        'data/ir_sequence_data.xml',
        'security/ir.model.access.csv',
        'views/faltas_nomina_view.xml',
        'views/vacaciones_nomina_view.xml',
        'views/incapacidades_view.xml',
        'views/incidencias_view.xml',
        'views/retardos_view.xml',
        'views/res_config_settings_views.xml',
        'views/templates.xml',
        'views/viaticos_nomina_view.xml',
        'wizard/crear_faltas_from_retardos.xml',
        'views/hr_payslip_view.xml',
        'security/security.xml',
        'views/hr_employee_view.xml',
        'views/hr_loan_view.xml',
        'views/ir_sequence_data.xml',
        'views/employee_loan_type_views.xml',
       # 'edi/mail_template.xml',
       # 'edi/skip_installment_mail_template.xml',
        'views/pay_slip_view.xml',
        'views/salary_structure.xml',
        'views/hr_contract_view.xml',
        'views/dias_feriados_view.xml',
        #'wizard/import_loan_views.xml',
        'wizard/import_logs_view.xml',
        'views/dev_skip_installment.xml',
        'report/report_paperformat.xml',
        'report/payslip_batches_report.xml',
        'views/employee_view.xml',
        'report/payslip_batches_pagos_report.xml',
        'report/payslip_batches_pagos_report2.xml',
        'report/payslip_batches_detail_report.xml',
        'report/listado_de_raya_report.xml',
        'wizard/wizard_reglas_salariales_view.xml',
        'wizard/calculo_isr_anual_view.xml', 
        'wizard/listado_de_nomina_wizard_view.xml',
        #'security/ir.model.access.csv',
        'report/calculo_isr_anual_report.xml',
        'wizard/importar_dias_wizard.xml',
        'report/reporte_isr_imss.xml',
        'report/reporte_de_control.xml',
        'report/report_payslip_nomina_x_3.xml',
        'wizard/altas_y_bajas_view.xml',
        'wizard/total_por_empleado_view.xml',
        'wizard/total_por_departamento_view.xml',
        'views/credito_infonavit_view.xml',
    ],

#     'external_dependencies' : {
#         'python' : ['tzlocal'],
#     },
    'installable': True,
    'application': False,
    'license': 'AGPL-3',
}
