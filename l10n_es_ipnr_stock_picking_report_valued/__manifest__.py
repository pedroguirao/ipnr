# Copyright 2024 Manuel Regidor <manuel.regidor@sygel.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{
    "name": "IPNR Report Picking Valued",
    "summary": "Show IPNR amount in valued stock pickings.",
    "version": "17.0.1.0.1",
    "license": "AGPL-3",
    "author": "Sygel, Pedroguirao, Odoo Community Association (OCA)",
    "category": "Stock",
    "website": "https://github.com/OCA/l10n-spain",
    "depends": [
        "stock_picking_report_valued",
        "l10n_es_ipnr_sale",
    ],
    "data": ["report/report_deliveryslip.xml"],
    "installable": True,
}
