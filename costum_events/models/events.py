from odoo import models, fields, api
class events(models.Model):
     _inherit = 'event.event'

     theme_event = fields.Char(string="Theme Event")
     event_orgnizer = _id = fields.Many2one('organizer', string='Event Orginizer')
     material_ids = fields.Many2many('materials',string='Custom Materials')
