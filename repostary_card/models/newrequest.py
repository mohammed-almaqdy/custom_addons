from odoo import models, fields, api

class  NewRequest(models.Model):
    _name = 'newrequest'   
    _inherit = 'updaterequest'
    
    request_number =fields.Integer(string='Request Number')
    name = fields.Char(string='Name')
    email = fields.Char(string='Email', required=True)
    card_balance =fields.Float(string='Card Balance')
    request_status = fields.Selection(string='Request Status' , selection=[('pending', 'Pending'), ('approved', 'Approved'),(('rejected', 'Rejected'))], default='pending')
    request_date = fields.Date(string='Request Date' , default=fields.Date.today)
    document_ids =  fields.Binary(string='Document')
     
    @api.model
    def create(self, vals):
        vals['request_number'] = self.env['ir.sequence'].next_by_code('newrequest')
        return super(NewRequest, self).create(vals)
    def button_pending(self):
        for rec in self:
            rec.write({'request_status': 'pending'})
    
    def button_approved(self):
        for rec in self:
            rec.write({'request_status': 'approved'})
        self.card_number.create({
            'beneficiary': self.create_uid.partner_id.id,
                'card_balance': self.card_balance,
                'note': self.note,
                'card_date': self.request_data,   
        })
        templete = self.env.ref('repostary_card.myemail_temp')
        self.env['mail.template'].browse(templete.id).send_mail(self.id, force_send=True)
        
    def button_rejected(self):
        for rec in self:
            rec.write({'request_status': 'rejected'})
    
    
        