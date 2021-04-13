# Copyright 2021 - Carlos Reyes <carlos@studio73.es>
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).
from odoo import api, fields, models


class HelpdeskTicket(models.Model):
    _name = "helpdesk.ticket"
    _description = "Task management"
    _inherits = {"project.task": "task_id"}

    task_id = fields.Many2one(
        comodel_name="project.task",
        string="Task",
        auto_join=True,
        index=True,
        ondelete="cascade",
        required=True,
    )
    corrective_action = fields.Html(string="Corective Action")
    preventive_action = fields.Html(string="Preventive Action")

    def action_assign_to_me(self):
        self.ensure_one()
        return self.task_id.action_assign_to_me()

    def action_subtask(self):
        self.ensure_one()
        return self.task_id.action_subtask()

    def action_recurring_tasks(self):
        self.ensure_one()
        return self.task_id.action_recurring_tasks()

    def _message_get_suggested_recipients(self):
        self.ensure_one()
        return self.task_id._message_get_suggested_recipients()

    def action_view_so(self):
        self.ensure_one()
        return self.task_id.action_view_so()

    @api.model
    def _default_get(self, fields):
        defaults = super()._default_get(fields)
        defaults.update(
            {
                "project_id": self.env.ref(
                    "profect_helpdesk_reyes4711.project_helpdesk"
                ).id
            }
        )
