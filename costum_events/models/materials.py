from odoo import models, fields, api
class materials(models.Model):
    _name='materials'
    
    name=fields.Char(string='name of equepment')
    department=fields.Char()
    
    
    