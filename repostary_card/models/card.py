from odoo import models, fields, api
from datetime import datetime, date

class Card(models.Model):
    _name = 'card'
    _rec_name = 'beneficiary'
    
    card_number = fields.Char(string='Card Number' , readonly=True)
    beneficiary =  fields.Many2one('res.partner', string='Beneficiary',)
    status =  fields.Selection( string='Status',selection=[('active', 'Active'),('expired', 'Expired'), ('canceld', 'Canceld')], default='active')
    card_date = fields.Date(string='Card Date' , default=fields.Date.today)
    expired_date = fields.Date(string='Expired Date')
    card_balance = fields.Integer(string='Card Balance', default=100)
    note  = fields.Text(string='Note')
    @api.model
    def create(self, vals):
        vals['card_number'] = self.env['ir.sequence'].next_by_code('card')
        return super(Card, self).create(vals)
    
   
    def button_done(self):
        for rec in self:
            rec.write({'status': 'active'})
    
    def button_cancel(self):
        for rec in self:
            rec.write({'status': 'canceld'})
    
    def check_expired(self):
       today = fields.Date.today()
       purchase_orders = self.env['card'].search([])
       for order in purchase_orders:
           if order.status == 'active' and order.expired_date < today:
               order.status = 'expired'
   