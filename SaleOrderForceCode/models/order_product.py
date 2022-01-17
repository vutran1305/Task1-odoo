from odoo import models , fields ,api


class OrderProduct(models.Model):
    _name = "order.product"
    _description = "order product"
    customer_order = fields.Many2one('customer', 'customer_order')
    quantity = fields.Integer(string = "Quantity" , default = 0)
    total =     fields.Float(string = "Total" , default = 0 )
    Sale_order_discount_estimated = fields.Float(string ="Sale order discount estimated" , default = 0 )
    priceOneProduct = fields.Float(string = "Price of one product" , default = 0 )
    payment = fields.Float(string = "Total payment" )
    discount_code = fields.Text(string ="Discount code" , related = "customer_order.code")
    order_valid = fields.Boolean('Order Valid', default=False)


    @api.onchange('quantity', 'priceOneProduct' , 'customer_order','discount_code')
    def _onchange_code(self):
        if not self.quantity  or not self.customer_order or not  self.priceOneProduct or self.customer_order.code_valid == False:
            self.total = self.priceOneProduct * float(self.quantity)
            self.Sale_order_discount_estimated = 0
            self.payment = self.total
            self.discount_code = self.customer_order.code
        else:
            self.order_valid = self.customer_order.code_valid
            self.discount_code = self.customer_order.code
            self.total = self.priceOneProduct * float(self.quantity)
            last = self.customer_order.code
            last = float(last[4:len(last)])*1.0
            self.Sale_order_discount_estimated = (self.total * last )/100.0
            self.payment = self.total - self.Sale_order_discount_estimated

