from odoo import models , fields ,api
from odoo.exceptions import UserError, ValidationError
import json
class OrderProduct(models.Model):
    _inherit = "sale.order"
    Sale_order_discount_estimated = fields.Float(string ="Sale order discount estimated" , default = 0 , related = 'partner_id.Sale_order_discount_estimated')
    customer_discount_code = fields.Char(string ="Discount code" , related = "partner_id.customer_discount_code")
    discout_order_check = fields.Boolean('Order Valid', default=False , related = "partner_id.code_valid")




    @api.depends('order_line.tax_id', 'order_line.price_unit', 'amount_total', 'amount_untaxed','Sale_order_discount_estimated' )
    def _compute_tax_totals_json(self):
        def compute_taxes(order_line):
            price = order_line.price_unit * (1 - (order_line.discount or 0.0) / 100.0)
            order = order_line.order_id
            return order_line.tax_id._origin.compute_all(price, order.currency_id, order_line.product_uom_qty,
                                                         product=order_line.product_id,
                                                         partner=order.partner_shipping_id)

        account_move = self.env['account.move']
        for order in self:
            tax_lines_data = account_move._prepare_tax_lines_data_for_totals_from_object(order.order_line,
                                                                                         compute_taxes)
            tax_totals = account_move._get_tax_totals(order.partner_id, tax_lines_data, order.amount_total,
                                                      order.amount_untaxed, order.currency_id)

            tax_totals["amount_total"] = tax_totals["amount_total"]  * (1 - (self.Sale_order_discount_estimated) / 100.0)
            tax_totals["formatted_amount_total"] = '$ ' + str(tax_totals["amount_total"])
            tax_totals["amount_untaxed"] = tax_totals["amount_untaxed"]  * (1 - (self.Sale_order_discount_estimated) / 100.0)
            tax_totals["formatted_amount_untaxed"] = '$ ' + str(tax_totals["amount_untaxed"])
            order.tax_totals_json = json.dumps(tax_totals)



