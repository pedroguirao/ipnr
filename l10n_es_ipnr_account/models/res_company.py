# Copyright 2023 Manuel Regidor <manuel.regidor@sygel.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import _, api, fields, models
from odoo.exceptions import ValidationError


class ResCompany(models.Model):
    _inherit = "res.company"

    ipnr_enable = fields.Boolean()
    ipnr_date_from = fields.Date(help="IPNR can only be applied from this date.")
    ipnr_show_in_reports = fields.Boolean(
        string="Show detailed IPNR amount in report lines",
        help="If active, IPNR amount is shown in reports.",
    )

    @api.constrains("ipnr_enable", "ipnr_date_from")
    def _check_pnr_date(self):
        if self.filtered(lambda a: a.ipnr_enable and not a.ipnr_date_from):
            raise ValidationError(
                _("'Ipnr Date From' is mandatory for companies with IPNR enabled.")
            )
