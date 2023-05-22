from odoo import models, fields
class plane_aeroport(models.Model):
    _name = 'plane.aeroport'
    location = fields.Char(compute='_gete_locaion', string='Localitzacio', readonly='True', store=False)
    nom = fields.Char('Nom')
    imatge = fields.Char('Imatge')
    ciutat = fields.Char('Ciutat')
    pais = fields.Char('Pais')
    latitud = fields.Float('Latitud')
    longitud = fields.Float('Longitud')
    desti_ids = fields.One2many('plane.vol','desti_id', string='VolDesti')
    origen_ids = fields.One2many('plane.vol','origen_id', string='VolOrigen')

def _get_location(selt):
    for record in self:
        record.location = str(record.pais) + " " + str(record.ciutat)