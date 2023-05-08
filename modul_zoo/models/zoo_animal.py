from odoo import models, fields
class zoo_animal(models.Model):
    _name = 'zoo.animal'
    id = fields.Integer('Id animal', required=True)
    continentorigen = fields.Char('Continent d''origen')
    datanaix = fields.Date('Data de naixament')
    paisorigen = fields.Char('Lloc de naixament')
    sexe = fields.Char('Sexe')