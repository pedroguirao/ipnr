# Copyright 2023 Manuel Regidor <manuel.regidor@sygel.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{
    "name": "IPNR - Ventas",
    "summary": "Impuesto especial sobre los envases de plástico no reutilizables España - Ventas",
    "version": "17.0.1.0.1",
    "license": "AGPL-3",
    "author": "Sygel, Odoo Community Association (OCA)",
    "category": "Accounting",
    "website": "https://github.com/OCA/l10n-spain",
    "depends": ["l10n_es_ipnr_account", "sale"],
    "data": [
        "data/exception_templates.xml",
        "views/sale_order_views.xml",
        "report/ir_actions_report_templates.xml",
    ],
    "pre_init_hook": "pre_init_hook",
    "installable": True,
}
