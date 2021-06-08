from odoo import models, fields, api
class Partner(models.Model):
    _inherit = 'res.partner'
    
    is_orgnization = fields.Boolean( string='Is Orgnization')
    