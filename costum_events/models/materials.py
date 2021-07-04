from odoo import models, fields, api
class Material(models.Model):
    _name='materials'
    
    name=fields.Char(string='Name of Equepment')
    type = fields.Selection(
        string='Type',
        selection=[('sound_equepment', 'Sound Equepment'), ('projection_equepment', 'Projection Equepment')])
    
    
    
    