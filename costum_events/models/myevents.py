from odoo import models, fields, api
class Myevent(models.Model):
     _inherit = 'event.event'
     _rec_name = 'myevents'

     theme_event = fields.Char(string="Theme Event")
     event_orgnizer = fields.One2many('organizer.organizer', 'orgnizer_ids', string='Event Orginizer')
     material_ids = fields.Many2many('materials.materials',string='Custom Materials')
