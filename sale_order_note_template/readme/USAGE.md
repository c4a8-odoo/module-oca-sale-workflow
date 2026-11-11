Go to *Sales > Configuration > Terms and conditions Templates* and create a
template.

To insert sale order values in the text:

- type `/` in the editor and choose *Dynamic Placeholder*, then pick the
  field to insert (and optionally a default value shown when the field is
  empty), or
- write inline placeholders by hand, e.g.
  `{{ object.client_order_ref ||| none provided }}` or
  `{{ format_amount(object.amount_total, object.currency_id) }}`.

Both syntaxes can be mixed in the same template. The placeholders are
resolved when the template is selected on a quotation; the resulting text is
stored in the quotation's *Terms and conditions* and is not updated
afterwards.

Only a few simple placeholders (order name, customer name, salesperson
name) are allowed for every user. Templates using other expressions
(default values, formatting helpers, computations...) can only be applied
by users belonging to the *Mail Template Editor* group.
