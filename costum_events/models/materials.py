from odoo import models, fields, api
class Material(models.Model):
    _name='materials.materials'
    
    name=fields.Char(string='Name of Equepment')
    characterize = fields.Char()
    
    
    