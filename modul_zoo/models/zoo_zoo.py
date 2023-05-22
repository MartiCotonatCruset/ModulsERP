from odoo import models, fields
class zoo_zoo(models.Model):
    _name = 'zoo.zoo'
    location = fields.Char(compute='_gete_locaion', string='Localitzacio', readonly='True', store=False)
    grandaria = fields.Float('Grandaria')
    nom = fields.Char('Nom')
    ciutat = fields.Char('Ciutat')
    pais = fields.Char('Pais')
    animal_ids = fields.One2many('zoo.animal','zoo_id', string='Animals')

def _get_location(selt):
    for record in self:
        record.location = str(record.pais) + " " + str(record.ciutat)