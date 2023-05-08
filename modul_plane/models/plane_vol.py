from odoo import models, fields
class plane_vol(models.Model):
    _name = 'plane.vol'
    codi = fields.Integer('Codi', required=True)
    passatger = fields.Integer('Passatgers')
    datasortida = fields.Date('Data sortida')
    dataarrivada = fields.Data('Data arrivada')