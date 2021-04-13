# Copyright 2021 - Carlos Reyes <carlos@studio73.es>
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).
from odoo import api, fields, models


class HelpdeskTicketTag(models.Model):
    _name = "helpdesk.ticket.tag"
    _description = "Helpdesk basical ticket tag"

    name = fields.Char(string="Name")
    tag_ids = fields.Many2many(
        comodel_name="helpdesk.ticket",
        relation="helpdesk_ticket_tag_rel",
        column1="tag_id",
        column2="ticket_id",
        string="Tags",
    )

    @api.model
    def cron_delete_tag(self):
        tags = self.search([("tag_ids", "=", False)])
        tags.unlink()
