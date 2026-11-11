# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
from odoo.addons.base.tests.common import BaseCommon


class TestSaleTermsTemplate(BaseCommon):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.term_template = cls.env["sale.terms_template"].create(
            {
                "name": "My terms and conditions template",
                "text": "<p>Terms template {{ object.partner_id.name }}</p>",
            }
        )
        cls.sale_order = cls.env["sale.order"].create(
            {
                "partner_id": cls.partner.id,
                "client_order_ref": "REF-42",
            }
        )

    def test_get_value(self):
        self.assertEqual(
            self.term_template.get_value(self.sale_order),
            f"<p>Terms template {self.partner.name}</p>",
        )

    def test_get_value_with_translation(self):
        # Ensure 'fr_BE' is loaded
        self.env["res.lang"]._activate_lang("fr_BE")
        self.sale_order.partner_id.lang = "fr_BE"

        # We need to translate the 'text' field of the template
        self.term_template.with_context(lang="fr_BE").write(
            {"text": "<p>Testing translated fr_BE {{ object.partner_id.name }}</p>"}
        )

        # Verify rendered value for the order in fr_BE
        rendered = self.term_template.get_value(self.sale_order)
        self.assertEqual(
            rendered,
            f"<p>Testing translated fr_BE {self.partner.name}</p>",
        )

    def test_render_model(self):
        """The dynamic placeholder selector must be fed with the sale order model."""
        self.assertEqual(self.term_template.render_model, "sale.order")

    def test_qweb_placeholder_kept_by_sanitizer(self):
        """``<t t-out>`` tags inserted by the editor must survive the write."""
        self.term_template.text = (
            '<p>Hello <t t-out="object.partner_id.name">Customer</t></p>'
        )
        self.assertIn('<t t-out="object.partner_id.name">', self.term_template.text)

    def test_get_value_qweb_placeholder(self):
        """Placeholders inserted with the editor's Dynamic Placeholder command."""
        self.term_template.text = (
            '<p>Order <t t-out="object.name"/> for '
            '<t t-out="object.partner_id.name">Customer</t></p>'
        )
        self.assertEqual(
            self.term_template.get_value(self.sale_order),
            f"<p>Order {self.sale_order.name} for {self.partner.name}</p>",
        )

    def test_get_value_qweb_placeholder_default(self):
        """The tag content is used as default value when the field is empty."""
        self.sale_order.client_order_ref = False
        self.term_template.text = (
            '<p>Ref: <t t-out="object.client_order_ref">none provided</t></p>'
        )
        self.assertEqual(
            self.term_template.get_value(self.sale_order),
            "<p>Ref: none provided</p>",
        )

    def test_get_value_mixed_syntax(self):
        """Inline and qweb placeholders can be mixed in the same template."""
        self.term_template.text = (
            '<p><t t-out="object.name"/> - {{ object.client_order_ref ||| none }} - '
            "{{ object.partner_id.name }}</p>"
        )
        self.assertEqual(
            self.term_template.get_value(self.sale_order),
            f"<p>{self.sale_order.name} - REF-42 - {self.partner.name}</p>",
        )

    def test_get_value_inline_default(self):
        self.sale_order.client_order_ref = False
        self.term_template.text = (
            "<p>{{ object.client_order_ref ||| none provided }}</p>"
        )
        self.assertEqual(
            self.term_template.get_value(self.sale_order),
            "<p>none provided</p>",
        )

    def test_get_value_inline_escaped_operator(self):
        """The Html field stores ``<``/``>`` as entities; expressions still work."""
        self.term_template.text = (
            "<p>{{ 'big' if len(object.name) > 1 else 'small' }}</p>"
        )
        self.assertIn("&gt;", self.term_template.text)
        self.assertEqual(self.term_template.get_value(self.sale_order), "<p>big</p>")
