# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo.tests.common import HttpCase, tagged

from odoo.addons.base.tests.common import BaseCommon


@tagged("post_install", "-at_install")
class TestSaleOrderArchiveUi(BaseCommon, HttpCase):
    def _save_screencast(self):
        pass

    def test_01_sale_tour(self):
        assert self.env["ir.module.module"].search(
            [("name", "=", "sale_management"), ("state", "=", "installed")]
        ), "Module 'sale_management' must be installed"

        self.start_tour(
            "/web",
            "sale_order_archive_tutorial",
            login="admin",
            step_delay=150,
            screencast=False,
        )
