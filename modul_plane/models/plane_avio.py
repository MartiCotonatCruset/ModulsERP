from odoo import models, fields
class plane_avio(models.Model):
    _name = 'plane.avio'
    nom = fields.Char(compute="_get_nom", strin="Nom complet", readonly="True", sotre=False)
    imatge = fields.Char('Imatge')
    marca = fields.Integer('Marca')
    model = fields.Char('Model')
    maxvel = fields.Float('Velocitat maxima')
    vol_ids = fields.One2many('plane.vol','avio_id', string='Vols')

def _get_nom(self):
    for record in self:
        record.nom = str(record.marca) + " " + str(record.model)