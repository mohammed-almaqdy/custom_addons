from odoo import models, fields, api

class  UpdateRequest(models.Model):
    _name = 'updaterequest'
    _rec_name = 'card_number'
    
    card_number = fields.Many2one('card',string='Card')
    request_number = fields.Integer(string='Request Number')
    request_status = fields.Selection(string='Request Status' , selection=[('value1', 'pending'), ('value2', 'approved'),(('value3', 'rejected'))], default='value1')
    request_date = fields.Date(string='Request Date' , default=fields.Date.today)
    request_type = fields.Selection([('val1', 'activated'),('val2', 'canceled')])
    
    @api.model
    def create(self, vals):
        vals['card_number'] = self.env['ir.sequence'].next_by_code('updaterequest')
        return super(UpdateRequest, self).create(vals)
    
    def button_pending(self):
        for rec in self:
            rec.write({'request_status': 'value1'})
    
    def button_approved(self):
        for rec in self:
            rec.write({'request_status': 'value2'})
    def button_rejected(self):
        for rec in self:
            rec.write({'request_status': 'value3'})
    @api.onchange('card_number')
    def _onchange_card(self):
        for request in self:
            request.status = 'value3' if request.status == 'value1' else 'value1'
    @api.depends('card_number')
    def _compute_number(self):
        for request in self:
            request.status = 'value3' if request.status == 'value1' else 'value1'
            