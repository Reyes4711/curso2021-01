# Copyright 2021 - Carlos Reyes <carlos@studio73.es>
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).
from odoo import fields, models


class ProductProduct(models.Model):
    _inherit = "product.product"

    tag_id = fields.Many2one(comodel_name="helpdesk.ticket.tag", string="Tag")
