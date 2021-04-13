# Copyright 2021 Studio73 - Carlos Reyes <carlos@studio73.es>
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo.tests.common import TransactionCase
from odoo.exceptions import ValidationError


class TestHelpdeskReyes4711(TransactionCase):
    def setUp(self):
        super().setUp()
        self.user = self.env.ref("base.user_admin")
        self.ticket = self.env["helpdesk.ticket"].create({"name": "test ticket"})

    def test_ticket(self):
        self.assertEqual(self.ticket.name, "test ticket", "el nombre no coincide")
        self.ticket.update({"user_id": self.user.id})
        self.assertEqual(
            self.ticket.user_id, self.user.name, "el usuario no es correcto"
        )

    def test_dedicated_time(self):
        self.ticket.update({"time": 2.00})
        self.assertEqual(self.ticket.time, 2.00, "Tiempo correcto")
        with self.assertRaises(ValidationError):
            self.ticket.update({"time": -3.00})
