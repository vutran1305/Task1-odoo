from odoo import models , fields ,api
from odoo.exceptions import UserError, ValidationError
import json
class OrderProduct(models.Model):
    _inherit = "sale.order"
    Sale_order_discount_estimated = fields.Float(string ="Sale order discount estimated" , default = 0 , related = 'partner_id.Sale_order_discount_estimated')
    customer_discount_code = fields.Char(string ="Discount code" , related = "partner_id.customer_discount_code")
    discout_order_check = fields.Boolean('Order Valid', default=False , related = "partner_id.code_valid")




    # @api.onchange('order_line' , 'Sale_order_discount_estimated' )
    # def _compute_discount_estimated(self):
    #     for record in self:
    #         sum = 0
    #         for line in record.order_line:
    #             sum += line.price_subtotal
    #         record.amount_total = sum -  sum * (record.Sale_order_discount_estimated)/ 100.0

    @api.depends('order_line.price_total', 'Sale_order_discount_estimated')
    def _amount_all(self):
        res = super(OrderProduct,self)
        for order in self:
            amount_untaxed = 0.0
            amount_tax = 0.0
            for line in order.order_line:
                amount_untaxed += line.price_subtotal
                amount_tax += line.price_tax
            order.update({
                'amount_untaxed': amount_untaxed,
                'amount_tax': amount_tax,
                'amount_total': (amount_untaxed + amount_tax) - (amount_untaxed + amount_tax)* (order.Sale_order_discount_estimated)/ 100.0  ,
            })
        return res







