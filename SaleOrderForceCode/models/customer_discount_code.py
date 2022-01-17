from odoo import models , fields ,api
from odoo.exceptions import UserError, ValidationError
class Customer(models.Model):
    _name = "customer"
    _description = "Customer "
    name  = fields.Char("Customer name" )
    gender = fields.Selection([('male','Male') ,('female','Female')],string = 'Gender', default = 'male')
    birthday = fields.Date('Birthday', required=False)
    code = fields.Text('code')
    code_valid = fields.Boolean('Sale code Valid', default=False)
    order_id = fields.One2many('order.product' , 'customer_order', string = "Order")

    @api.onchange('code')
    def _onchange_code(self):
        if not self.code :

            return {}
        else :
            self.order_id.discount_code = self.code
            if  len(self.code) < 5:
                self.code_valid = False
            else:
                fist = self.code[0:4]
                last = self.code[4:len(self.code)]
                if fist == "VIP_" and len(last) < 3 and last.isdigit():
                    self.code_valid = True
                else :
                    self.code_valid = False



    @api.model
    def checkcode(self, code):
        fist = code[0:4]
        last = code[4:len(code)]
        if fist == "VIP_" and len(last) < 3 and last.isdigit():
            return True
        else:
            return False





