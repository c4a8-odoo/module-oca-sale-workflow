This module add sale terms and conditions templates and change existing
terms and conditions (sale_order.note) field type from Text to Html.

Users will be able to select *terms and conditions template* to fulfill
*terms and conditions*. Like in mail templates, the template text can
reference values of the sale order: use the *Dynamic Placeholder* command
of the editor (type `/` in the text) to pick a field, or write inline
placeholders such as `{{ object.partner_id.name }}` by hand.

## How this module differ from [sale_comment_template](https://github.com/OCA/sale-reporting/tree/14.0/sale_comment_template)?

- [base_comment_template](https://github.com/OCA/reporting-engine/tree/14.0/base_comment_template)
  is for managing comments not terms, it would probably see as mess for
  users to mixed terms and comments.
- [sale_comment_template](https://github.com/OCA/sale-reporting/tree/14.0/sale_comment_template)
  depends on
  [account_comment_template](https://github.com/OCA/account-invoice-reporting/tree/14.0/account_comment_template)
  comments are forwards to generated invoices, here we don't really
  display sales terms on final invoices
- [base_comment_template](https://github.com/OCA/reporting-engine/tree/14.0/base_comment_template)
  at the time writing do not support template engine
