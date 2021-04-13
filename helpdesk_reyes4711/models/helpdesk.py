# Copyright 2021 - Carlos Reyes <carlos@studio73.es>
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).
from odoo import _, api, fields, models
from datetime import date, timedelta
from odoo.exceptions import ValidationError


class HelpdeskTicket(models.Model):
    _name = "helpdesk.ticket"
    _description = "Helpdesk basical ticket"
    _inherit = ["mail.activity.mixin", "mail.thread.cc", "mail.thread.blacklist"]
    _primary_email = "email_from"

    def _date_default_today(self):
        return fields.date.today()

    name = fields.Char(string="Name", required=True, translate=True)
    description = fields.Text()
    creation_date = fields.Date(string="Creation Date", default=_date_default_today)
    state = fields.Selection(
        string="State",
        selection=[
            ("new", "New"),
            ("asigned", "Asigned"),
            ("inprocess", "In Process"),
            ("pending", "Pending"),
            ("approved", "Approved"),
            ("cancel", "Cancel"),
        ],
        default="new",
    )
    asigned = fields.Boolean(string="Asigned", compute="_compute_asigned")
    limit_date = fields.Date(string="Limit Date", help="Limit date to do this")
    time = fields.Float(
        string="Used Time",
        compute="_get_time",
        inverse="_set_time",
        search="_search_time",
    )
    corrective_action = fields.Html(string="Corective Action")
    preventive_action = fields.Html(string="Preventive Action")
    action_ids = fields.One2many(
        comodel_name="helpdesk.ticket.action",
        inverse_name="helpdesk_id",
        string="Helpdesk Actions",
    )
    user_id = fields.Many2one(comodel_name="res.users", string="Assigned to")
    tag_ids = fields.Many2many(
        comodel_name="helpdesk.ticket.tag",
        relation="helpdesk_ticket_tag_rel",
        column1="ticket_id",
        column2="tag_id",
        string="Tags",
    )
    ticket_qty = fields.Integer(string="Ticket Quantity", compute="_compute_ticket_qty")
    tag_name = fields.Char(string="Tag name")
    color = fields.Integer(string="Color")
    partner_id = fields.Many2one(comodel_name="res.partner", string="Partner")
    email_from = fields.Char(string="Email From")

    def _search_time(self, operator, value):
        actions = self.env["helpdesk.ticket.action"].search([("time", operator, value)])
        return [("id", "in", action.mapped("ticket_id").ids)]

    @api.depends("action_ids.time")
    def _get_time(self):
        for record in self:
            record.time = sum(record.action_ids.mapped("time"))

    def _set_time(self):
        for record in self:
            if record.time:
                time_now = sum(record.action_ids.mapped("time"))
                next_time = record.time - time_now
                if next_time:
                    data = {
                        "name": "Action_1",
                        "time": next_time,
                        "creation_date": fields.Date.today(),
                        "helpdesk_id": record.id,
                    }
                    self.env["helpdesk.ticket.action"].create(data)

    @api.onchange("creation_date")
    def _onchange_creation_date(self):
        self.limit_date = self.creation_date + timedelta(days=1)

    @api.constrains("time")
    def _constrain_time(self):
        for ticket in self:
            if ticket.time and ticket.time < 0:
                raise ValidationError(_("The value must be higher than 0"))

    @api.depends("user_id")
    def _compute_asigned(self):
        for record in self:
            record.asigned = self.user_id and True or False

    @api.depends("user_id")
    def _compute_ticket_qty(self):
        for record in self:
            other_tickets = self.env["helpdesk.ticket"].search(
                [("user_id", "=", record.user_id.id)]
            )
            record.ticket_qty = len(other_tickets)

    def action2asing(self):
        self.ensure_one()
        return self.write({"state": "asigned", "asigned": True})

    def action2inprocess(self):
        self.ensure_one()
        return self.write({"state": "inprocess"})

    def action2pending(self):
        self.ensure_one()
        return self.write({"state": "pending"})

    def action2finish(self):
        self.ensure_one()
        return self.write({"state": "approved"})

    def action2cancel(self):
        self.ensure_one()
        return self.write({"state": "cancel"})

    def action2cancel_multi(self):
        for record in self:
            record.action2cancel()

    def create_tag(self):
        self.ensure_one()
        # self.write({"tag_ids": [(0, 0, {"name": self.tag_name})]})
        action = self.env.ref("helpdesk_reyes4711.action_new_tag").read()[0]
        action["context"] = {
            "default_name": self.tag_name,
            "default_ticket_ids": [(6, 0, self.ids)],
        }
        self.tag_name = False
        return action
