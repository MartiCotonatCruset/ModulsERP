from odoo import models, fields
class zoo_especie(models.Model):
    _name = 'zoo.especie'
    nom = fields.Char(compute='_get_nom', string="Nom complet", readonly='True', store=False)
    familia = fields.Char('Familia')
    nomcientific = fields.Char('Nom cientific')
    nombulgar = fields.Char('Nom bulgar')
    perill = fields.Char('Perill')
    animal_ids = fields.One2many('zoo.animal','especie_id', string='Animals')

def _get_nom(self):
    for record in self:
        record.nom = str(record.nombulgar) + "(" + str(record.nomcientific) + ")"