
# -*- coding: utf-8 -*-
from odoo import models, fields
class Organizer(models.Model):
    _name='organizer.organizer'
    _rec_name = 'organizers'
    
    firstname = fields.Char(Required =True)
    lastname = fields.Char(Required =True)
    phone = fields.Char()
    mail = fields.Char()
    orgnizer_ids = fields.Many2one('event.event', string='Manage Event')
   
