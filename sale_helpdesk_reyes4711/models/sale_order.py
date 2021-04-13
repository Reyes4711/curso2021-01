# Copyright 2021 - Carlos Reyes <carlos@studio73.es>
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).
from odoo import _, api, fields, models
from datetime import date, timedelta
from odoo.exceptions import ValidationError


class SaleOrder(models.Model):
    _inherit = "sale.order"

    ticket_ids = fields.One2many(
        comodel_name="helpdesk.ticket", inverse_name="sale_id", string=""
    )

    def create_ticket(self):
        self.ensure_one()
        tag_ids = self.order_line.mapped("product_id.tag_id")
        self.env["helpdesk.ticket"].create(
            {
                "name": "%s Issue" % (self.name),
                "tag_ids": [(6, 0, tag_ids)],
                "sale_id": self.id,
            }
        )

    def action_cancel(self):
        self.ticket_ids.action2cancel_multi()
        return super().action_cancel()
