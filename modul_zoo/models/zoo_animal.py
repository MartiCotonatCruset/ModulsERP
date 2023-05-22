from odoo import models, fields
class zoo_animal(models.Model):
    _name = 'zoo.animal'
    origen = fields.Char(compute='_get_origen', string="Origen", readonly='True', store=False)
    continentorigen = fields.Char('Continent d''origen')
    datanaix = fields.Date('Data de naixament')
    paisorigen = fields.Char('Lloc de naixament')
    sexe = fields.Char('Sexe')
    zoo_id = fields.Many2one('zoo.zoo', string='Zoo')
    especie_id = fields.Many2one('zoo.especie', string='Especie')

    def _get_origen(self):
        for record in self:
            record.origen = str(record.continentorigen) + " " + str(record.paisorigen)