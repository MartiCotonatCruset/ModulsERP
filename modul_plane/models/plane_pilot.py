from odoo import models, fields
class plane_pilot(models.Model):
    _name = 'plane.pilot'
    name = fields.Char(compute="_get_name", strin="Nom complet", readonly="True", store=False)
    nom = fields.Char('Nom')
    cognoms = fields.Char('Cognoms')
    nif = fields.Char('NIF')
    telf = fields.Char('Telf')
    email = fields.Char('Email')
    vol_ids = fields.One2many('plane.vol','pilot_id', string='Vols')

def _get_name(self):
    for record in self:
        record.name = str(record.nom) + " " + str(record.cognoms)