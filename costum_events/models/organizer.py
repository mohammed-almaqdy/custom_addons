
# -*- coding: utf-8 -*-
from odoo import models, fields
class organizer(models.Model):
    _name='organizer'
    firstname=fields.Char(Required =True)
    lastname=fields.Char(Required =True)
    phone=fields.Char()
    mail=fields.Char()
    type1=fields.Selection(string='Organizer Type',selection=[('val1', 'person'), ('val2', 'company')],default='val1')
    # field1 = fields.Char(string='Field1')
    # field2 = fields.Char(string='Field2')
    company_name=fields.Char(string='Company Name')

    # Gender=fields.Selection()
    orgnizer_ids = fields.Many2one('event.event',string='manage event')
    # male=fields.boolean(defult = False)
    # female=fields.boolean(defult = False)
    # events = fields.many2one('myevents',string = 'reserved events')

