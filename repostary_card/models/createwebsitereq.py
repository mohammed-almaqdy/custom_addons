from odoo import models, fields, api

class  CreateWebsitereq(models.Model):
    _name = 'createwebsitereq'   
    
    email = fields.Char(string='Email')
    mobile = fields.Integer(string='Mobile')
    full_name = fields.Char(string='Full Name')
    card_balance = fields.Integer('string=Card balance',default=100)
    notes = fields.Text( string='Notes')
    
    
    
    