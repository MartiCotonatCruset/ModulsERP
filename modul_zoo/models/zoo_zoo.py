from odoo import models, fields
class zoo_zoo(models.Model):
    _name = 'zoo.zoo'
    id = fields.Integer('Id zoo', required=True)
    grandaria = fields.Float('Grandaria')
    nom = fields.Date('Nom')
    ciutat = fields.Char('Ciutat')
    pais = fields.Char('Pais')