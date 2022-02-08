from odoo import api, fields, models, tools, _
from odoo.exceptions import UserError, ValidationError

import logging

_logger = logging.getLogger(__name__)


class SaleCodeUpdateWizard(models.TransientModel):
    _name = "sale.code.update.wizard"
    customer_discount_code = fields.Char('Discount code')
    code_valid = fields.Boolean('Sale code Valid', default=False)


    def multi_update_discount_code(self):
        ids = self.env.context['active_ids']  # selected record ids
        customers = self.env["res.partner"].browse(ids)
        check = self._check_discount_code(code=self.customer_discount_code)
        if self.customer_discount_code and check:
            new_data = {
                "customer_discount_code" : self.customer_discount_code,
                "code_valid" : check,
            }
            customers.write(new_data)
        else:
            raise ValidationError("Mã sale không hợp lệ")



    # check discount code input valid
    @api.model
    def _check_discount_code(self,code):
        if len(code) < 5:
            return False
        else:
            fist = code[0:4]
            last = code[4:len(code)]
            if fist == "VIP_" and len(last) < 3 and last.isdigit():
                return True
            else:
                return False



