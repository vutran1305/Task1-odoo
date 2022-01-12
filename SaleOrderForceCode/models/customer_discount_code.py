from odoo import models , fields ,api

class Customer(models.Model):
    _name = "customer"
    _description = "Customer "
    name  = fields.Char("Customer name" , required = True)
    gender = fields.Selection([('male','Male') ,('female','Fmeale')],string = 'Gender', default = 'male')
    birthday = fields.Date('DOB', required=False)
    code = fields.Text()
    code_valid = fields.Boolean('Sale code Valid', default=False)

    @api.onchange('code')
    def _onchange_code(self):
        if not self.code:
            return {}
        else :
            fist = self.code[0:4]
            last = self.code[4:len(self.code)]
            if fist == "VIP_" and len(last) < 3 and last.isdigit():
                self.code_valid = True
            else :
                self.code_valid = False

