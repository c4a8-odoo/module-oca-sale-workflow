# Copyright 2014 Guewen Baconnier (Camptocamp SA)
# Copyright 2013-2014 Nicolas Bessi (Camptocamp SA)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

import html

from markupsafe import Markup

from odoo import api, fields, models
from odoo.tools.rendering_tools import parse_inline_template


class SaleTermsTemplate(models.Model):
    _name = "sale.terms_template"
    _description = "Sale terms template"

    active = fields.Boolean(default=True)

    name = fields.Char(required=True)

    # ``email_outgoing`` keeps the ``<t t-out="..."/>`` tags inserted by the
    # editor's dynamic placeholder command; the default sanitizer strips them.
    text = fields.Html(
        string="Terms template", translate=True, sanitize="email_outgoing"
    )

    render_model = fields.Char(
        compute="_compute_render_model",
        help="Technical field: model used by the dynamic placeholder selector.",
    )

    def _compute_render_model(self):
        self.render_model = "sale.order"

    @api.model
    def _get_qweb_template_src(self, text):
        """Convert ``text`` to a QWeb template source.

        Both syntaxes are supported in the same template:

        * ``{{ object.name ||| default }}`` inline placeholders (legacy syntax)
          are converted to ``<t t-out="object.name">default</t>``;
        * ``<t t-out="..."/>`` tags, as inserted by the editor's *Dynamic
          Placeholder* command, are kept as is.

        As ``text`` is an Html field, ``<``, ``>`` and ``&`` are stored as
        entities; they are unescaped inside inline placeholders so that
        expressions like ``{{ 'a' if object.amount_total > 0 else 'b' }}``
        keep working.
        """
        parts = []
        for string, expression, default in parse_inline_template(Markup(text or "")):
            parts.append(string)
            if expression:
                parts.append(
                    Markup('<t t-out="{}">{}</t>').format(
                        html.unescape(expression), html.unescape(default).strip()
                    )
                )
        return Markup("").join(parts)

    def get_value(self, sale_order, add_context=None, post_process=True):
        """Get sales terms from template.

        Like in mail composer `text` template can use inline (``{{ }}``) or
        qweb (``<t t-out=""/>``) syntax.

        if `partner_id` is provide, it will retreive it's lang to use the
        right translation.

        Then template is populated with model/res_id attributes according
        inline/qweb instructions.

        :param sale_order: recordset (browsed) sale order
        :param add_context: context forwarded to the templating engine
        :param post_process: what ever to use `post_process` from the templating
                             engine. If `True` urls are transform to absolute urls
        """
        self.ensure_one()
        sale_order.ensure_one()
        lang = sale_order.partner_id.lang if sale_order.partner_id else None
        comment_texts = self.env["mail.render.mixin"]._render_template(
            template_src=self._get_qweb_template_src(self.with_context(lang=lang).text),
            model="sale.order",
            res_ids=[sale_order.id],
            engine="qweb",
            add_context=add_context,
            options={"post_process": post_process},
        )
        return comment_texts[sale_order.id] or ""
