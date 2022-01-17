from odoo import models , fields ,api


class OrderProduct(models.Model):
    _name = "order.product"
    _description = "order product"
    customer_order = fields.Many2one('customer', 'customer_order')
    quantity = fields.Integer(string = "Quantity" , default = 0)
    total =     fields.Float(string = "Total" , default = 0 , compute= '_total_payment')
    Sale_order_discount_estimated = fields.Float(string ="Sale order discount estimated" , default = 0 , compute= '_total_payment')
    priceOneProduct = fields.Float(string = "Price of one product" , default = 0 )
    payment = fields.Float(string = "Total payment" , compute= '_total_payment')
    discount_code = fields.Text(string ="Discount code" , related = "customer_order.code")
    order_valid = fields.Boolean('Order Valid', default=False)


    @api.onchange('quantity', 'priceOneProduct' , 'customer_order')
    def _onchange_code(self):
        if not self.quantity  or not self.customer_order or not  self.priceOneProduct or self.customer_order.code_valid == False:
            self.total = self.priceOneProduct * float(self.quantity)
            self.Sale_order_discount_estimated = 0
            self.payment = self.total
        else:
            self.order_valid = self.customer_order.code_valid
            self.total = self.priceOneProduct * float(self.quantity)
            discount = self.customer_order.code
            discount = float(discount[4:len(discount)])*1.0
            self.Sale_order_discount_estimated = (self.total * discount )/100.0
            self.payment = self.total - self.Sale_order_discount_estimated


    @api.depends('quantity','priceOneProduct','customer_order.code','discount_code')
    def _total_payment(self):
        for record in self:
            record.total = record.priceOneProduct * float(record.quantity)
            discount = record.discount_code
            discount = float(discount[4:len(discount)]) * 1.0
            record.Sale_order_discount_estimated = (record.total * discount) / 100.0
            record.payment = record.total - record.Sale_order_discount_estimated

