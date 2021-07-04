from odoo import models, fields, api

class  UpdateRequest(models.Model):
    _name = 'updaterequest'
    _rec_name = 'card_number'
    
    card_number = fields.Many2one('card',string='Card')
    request_number = fields.Integer(string='Request Number')
    request_status = fields.Selection(string='Request Status' , selection=[('pending', 'Pending'), ('approved', 'Approved'),(('rejected', 'Rejected'))], default='pending')
    request_date = fields.Date(string='Request Date' , default=fields.Date.today)
    request_type = fields.Selection([('val1', 'activated'),('val2', 'canceled')])
    
    @api.model
    def create(self, vals):
        vals['card_number'] = self.env['ir.sequence'].next_by_code('updaterequest')
        return super(UpdateRequest, self).create(vals)
    
    def button_pending(self):
        for rec in self:
            rec.write({'request_status': 'pending'})
    
    def button_approved(self):
        for rec in self:
            rec.write({'request_status': 'approved'})
    def button_rejected(self):
        for rec in self:
            rec.write({'request_status': 'rejected'})
    @api.onchange('card_number')
    def _onchange_card(self):
        for request in self:
            request.status = 'rejected' if request.status == 'pending' else 'pending'
    @api.depends('card_number')
    def _compute_number(self):
        for request in self:
            request.status = 'rejected' if request.status == 'pending' else 'pending'
            