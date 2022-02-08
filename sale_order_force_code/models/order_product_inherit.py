from odoo import models , fields ,api
from odoo.exceptions import UserError, ValidationError
import json
class OrderProduct(models.Model):
    _inherit = "sale.order"
    Sale_order_discount_estimated = fields.Float(string ="Sale order discount estimated" , default = 0 , related = 'partner_id.Sale_order_discount_estimated')
    customer_discount_code = fields.Char(string ="Discount code" , related = "partner_id.customer_discount_code")
    discout_order_check = fields.Boolean('Order Valid', default=False , related = "partner_id.code_valid")




    @api.onchange('order_line' , 'Sale_order_discount_estimated' )
    def _compute_discount_estimated(self):
        for record in self:
            sum = 0
            for line in record.order_line:
                sum += line.price_subtotal
            record.amount_total = sum * (1 - (record.Sale_order_discount_estimated) / 100.0)






