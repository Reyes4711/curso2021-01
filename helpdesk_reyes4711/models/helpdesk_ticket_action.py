# Copyright 2021 - Carlos Reyes <carlos@studio73.es>
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).
from odoo import fields, models


class HelpdeskTicketAction(models.Model):
    _name = "helpdesk.ticket.action"
    _description = "Helpdesk basical ticket actions"

    name = fields.Char(string="Name")
    creation_date = fields.Date(string="Creation Date")
    time = fields.Float(string="Time")

    helpdesk_id = fields.Many2one(comodel_name="helpdesk.ticket", string="Helpdesk")
