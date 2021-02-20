from odoo import models, fields, api


class discograficamulti_model(models.Model):
    _name = 'discografica.discografica_model'
    _inherit = 'discografica.discografica_model'
    _description = 'discograficamulti'


    director= fields.Many2one("res.partner","Director")