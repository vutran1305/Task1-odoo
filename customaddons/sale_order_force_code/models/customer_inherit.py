from odoo import models , fields ,api
from odoo.exceptions import UserError, ValidationError
class Customer(models.Model):
    _inherit = "res.partner"
    customer_discount_code = fields.Char('Discount Code')
    code_valid = fields.Boolean('Sale code Valid', default=False)
    Sale_order_discount_estimated = fields.Float("Discount estimated (%)"  , compute = '_calculator_discount_estimated')


    @api.onchange('customer_discount_code')
    def _onchange_discount_code(self):
        if not self.customer_discount_code :
            self.code_valid = False
        else :
            self.code_valid = self._check_discount_code(self.customer_discount_code)



    @api.model
    def _check_discount_code(self, customer_discount_code):
        if len(customer_discount_code) < 5:
            return False
        else:
            fist = customer_discount_code[0:4]
            last = customer_discount_code[4:len(customer_discount_code)]
            if fist == "VIP_"  and last.isdigit():
                return True
            else:
                return False

    @api.constrains('name','customer_discount_code')
    def _check_Validation(self):
        for record in self:
            if not record.name or not record.customer_discount_code :
                raise ValidationError("Vui lòng điền đúng các trường")

    # @api.onchange('customer_discount_code')
    def _calculator_discount_estimated(self):
        for record in self :
            if record.code_valid :
                record.Sale_order_discount_estimated = float(record.customer_discount_code[4:len(record.customer_discount_code)])
            else:
                record.Sale_order_discount_estimated = 0






