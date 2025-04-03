# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo.tests.common import HttpCase, tagged

from odoo.addons.base.tests.common import BaseCommon


@tagged("post_install", "-at_install")
class TestSaleOrderArchiveUi(BaseCommon, HttpCase):
    def test_01_sale_tour(self):
        self.start_tour(
            "/web", "sale_order_archive_tutorial", login="admin", step_delay=100
        )
