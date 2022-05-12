# Copyright 2021 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models

from .res_config import RESTRICT_DELETE_ATTACH


class IrAttachment(models.Model):
    _inherit = "ir.model"

    restrict_delete_attachment = fields.Selection(
        selection=RESTRICT_DELETE_ATTACH,
        compute="_compute_restrict_delete_attachment",
        readonly=True,
    )

    def _compute_restrict_delete_attachment(self):
        return (
            self.env["ir.config_parameter"]
            .sudo()
            .get_param("restrict_delete_attachment")
        )

    is_restrict_delete_attachment = fields.Boolean(
        string="Model with Restrict Attachment Deletion",
        help="When selected, the deletion of the attachments related to this model is "
        "restricted to certain users.",
    )

    delete_attachment_group_ids = fields.Many2many(
        "res.groups",
        string="Attachment Deletion Groups",
        help="The users in the groups selected here can delete the attachments related "
        "to this model.",
    )
    delete_attachment_user_ids = fields.Many2many(
        "res.users",
        string="Attachment Deletion Users",
        help="The users selected here can delete the attachments related to this "
        "model.",
    )
