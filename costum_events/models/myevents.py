# -*- coding: utf-8 -*-
from odoo import models, fields, api
class myevents(models.Model):
     
     _inherit = 'event.event'

     theme_event = fields.Char(string="Theme Event")
     event_orgnizer = fields.One2many('organizer','orgnizer_ids',string='event orginizer')
     material_tab = fields.Many2many('materials',string='material tab')
