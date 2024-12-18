# Copyright 2021-2024 Quartile
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl).

from odoo import _, api, fields, models
from odoo.exceptions import UserError


class ResUsers(models.Model):
    _inherit = "res.users"

    unrestrict_model_update = fields.Boolean(
        help="Set to true and the user can update restricted model.",
    )
    is_readonly_user = fields.Boolean(
        "Read-only User",
        help="Select this option to prevent the user from updating any business "
        "records.",
    )

    @api.constrains("is_readonly_user", "groups_id")
    def _check_is_readonly_user(self):
        for user in self:
            if user.has_group("base.group_system") and user.is_readonly_user:
                raise UserError(_("You cannot make the admin user read-only."))
