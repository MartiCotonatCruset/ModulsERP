from odoo import models, fields
class zoo_especie(models.Model):
    _name = 'zoo.especie'
    id = fields.Integer('Id especie', required=True)
    familia = fields.Char('Familia')
    nomcientific = fields.Date('Nom cientific')
    nombulgar = fields.Char('Nom bulgar')
    perill = fields.Char('Perill')