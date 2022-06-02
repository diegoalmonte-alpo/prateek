# -*- coding: utf-8 -*-

{
    'name': 'Cheque AP',
    'version': '1.0',
    'category': 'Localization',
    'summary': 'Print DR Checks',
    'description': """ """,
    'author': 'Alpo Multimedia, SRL',
    'website': '',
    'depends' : ['account','account_check_printing', 'l10n_us', 'l10n_us_check_printing'],
    
    'data': [
            'report/print_check_sisne.xml',
    ],
        
    'installable': True,
    'auto_install': False,
    'license': '',
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: