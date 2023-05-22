from odoo import models, fields
class plane_vol(models.Model):
    _name = 'plane.vol'
    data = fields.Char(compute='_get_data', string="Dates", readonly="True", store=False)
    passatger = fields.Integer('Passatgers')
    datasortida = fields.Datetime('Data sortida')
    dataarrivada = fields.Datetime('Data arrivada')
    desti_id = fields.Many2one('plane.aeroport', string='AeroportDesti')
    origen_id = fields.Many2one('plane.aeroport', string='AeroportOrigen')
    avio_id = fields.Many2one('plane.avio', string='Avio')
    pilot_id = fields.Many2one('plane.pilot', string='Pilot')

def _get_data(self):
    for record in self:
        record.data = str(record.datasortida) + " a " + str(record.dataarrivada)