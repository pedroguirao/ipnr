# Copyright 2023 Manuel Regidor <manuel.regidor@sygel.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{
    "name": "IPNR - Facturación",
    "summary": "Impuesto especial sobre los envases de plástico no reutilizables - Facturación",
    "version": "17.0.1.0.0",
    "license": "AGPL-3",
    "author": "Pedro guirao, Antonio Cánovas, Odoo Community Association (OCA)",
    "category": "Accounting",
    "website": "https://github.com/OCA/l10n-spain",
    "depends": ["account", 'l10n_es_aeat_mod592'],
    "data": [
        "data/data.xml",
        "data/exception_templates.xml",
        "security/ir.model.access.csv",
        "views/l10n_es_ipnr_amount_views.xml",
        "views/product_category_views.xml",
        "views/product_views.xml",
        "views/account_move_views.xml",
        "views/report_invoice.xml",
        "views/res_company_views.xml",
        "views/account_fiscal_position_views.xml",
    ],
    "pre_init_hook": "pre_init_hook",
    "installable": True,
}
