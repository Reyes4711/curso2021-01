# Copyright 2021 - Carlos Reyes <carlos@studio73.es>
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

{
    "name": "Helpdesk Reyes4711",
    "summary": "adds name as ticket",
    "version": "14.0.1.0.0",
    "license": "LGPL-3",
    "category": "Helpdesk",
    "author": "Carlos Reyes",
    "website": "https://www.github.com/Reyes4711",
    "depends": ["mail"],
    "data": [
        "security/helpdesk_security.xml",
        "security/ir.model.access.csv",
        "data/helpdesk_cron.xml",
        "report/helpdesk_ticket_report_templates.xml",
        "report/res_partner_templates.xml",
        "views/helpdesk_menu.xml",
        "wizard/create_ticket_view.xml",
        "views/helpdesk_tag_view.xml",
        "views/helpdesk_views.xml",
    ],
    "installable": True,
}
