
# -*- coding: utf-8 -*-
from odoo import models, fields
class Organizer(models.Model):
    _name = 'organizer'
    _rec_name = 'firstname'
    
    firstname = fields.Char(Required =True)
    lastname = fields.Char(Required =True)
    phone = fields.Char()
    mail = fields.Char()
   
