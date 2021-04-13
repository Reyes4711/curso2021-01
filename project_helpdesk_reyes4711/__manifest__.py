# Copyright 2021 - Carlos Reyes <carlos@studio73.es>
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

{
    "name": "Project Helpdesk Reyes4711",
    "summary": "adds name as ticket",
    "version": "14.0.1.0.0",
    "license": "LGPL-3",
    "category": "Helpdesk",
    "author": "Carlos Reyes",
    "website": "https://www.github.com/Reyes4711",
    "depends": ["project"],
    "data": [
        "security/helpdesk_security.xml",
        "security/ir.model.access.csv",
        "data/project_helpdesk_ticket.xml",
        "views/helpdesk_menu.xml",
        "views/helpdesk_ticket_view.xml",
    ],
    "installable": True,
}
