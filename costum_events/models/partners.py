from odoo import models, fields, api
class Partner(models.Model):
    _inherit = 'res.partner'
    _rec_name = 'partners'
    
    is_orgnizer = fields.Boolean(string='Is Orgnizer') 