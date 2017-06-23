# -*- coding: utf-8 -*-
##############################################################################
# For copyright and license notices, see __openerp__.py file in module root
# directory
##############################################################################
from openerp import fields, models


class StockMove(models.Model):
    _inherit = "stock.move"

    purchase_id = fields.Many2one(
        related='purchase_line_id.order_id',
        readonly=True,
    )