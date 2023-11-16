# Copyright 2014 Carlos Sánchez Cifuentes <csanchez@grupovermon.com>
# Copyright 2015-2020 Tecnativa - Pedro M. Baeza
# Copyright 2015 Oihane Crucelaegui <oihanecrucelaegi@avanzosc.es>
# Copyright 2016 Vicent Cubells <vicent.cubells@tecnativa.com>
# Copyright 2017 David Vidal <david.vidal@tecnativa.com>
# Copyright 2023 CRogos (glueckkanja AG)
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html
from odoo import models


class SaleOrder(models.Model):
    _inherit = "sale.order"

    def recalculate_prices(self):
        lines = self.mapped("order_line")
        lines._compute_discount()
        lines._compute_price_unit()
        return True

    def recalculate_names(self):
        lines = self.mapped("order_line")
        lines._compute_name()
        return True
