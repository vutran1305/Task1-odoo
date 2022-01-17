from odoo import api, fields, models, tools, _
from odoo.exceptions import UserError, ValidationError

import logging

_logger = logging.getLogger(__name__)


class SaleCodeUpdateWizard(models.TransientModel):
    _name = "sale.code.update.wizard"
    _description = "Update sale code customer"
    name = fields.Char("Customer name")
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string='Gender', default='male')
    birthday = fields.Date('Birthday', required=False)
    code = fields.Text('code')
    code_valid = fields.Boolean('Sale code Valid', default=False)
    order_id = fields.One2many('order.product', 'customer_order', string="Order")

    @api.onchange('code')
    def _onchange_code(self):
        if not self.code:
            return {}
        else:
            if len(self.code) < 5:
                self.code_valid = False
            else:
                fist = self.code[0:4]
                last = self.code[4:len(self.code)]
                if fist == "VIP_" and len(last) < 3 and last.isdigit():
                    self.code_valid = True
                else:
                    self.code_valid = False

    def multi_update(self):
        ids = self.env.context['active_ids']  # selected record ids
        customers = self.env["customer"].browse(ids)
        new_data = {}
        if self.code and self.checkcode(code=self.code):
            new_data["code"] = self.code
            new_data["code_valid"] = self.checkcode(code=self.code)
            customers.write(new_data)
        else:
            raise ValidationError("Mã sale không hợp lệ")




    @api.model
    def checkcode(self,code):
        if len(code) < 5:
            return False
        else:
            fist = code[0:4]
            last = code[4:len(self.code)]
            if fist == "VIP_" and len(last) < 3 and last.isdigit():
                return True
            else:
                return False



