# -*- coding: utf-8 -*-

from openerp import models, fields, api

class academy(models.Model):
    _name = 'course'

    name = fields.Char()
    value = fields.Text()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100
