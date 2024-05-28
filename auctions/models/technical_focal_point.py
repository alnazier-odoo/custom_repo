from odoo import fields, models, api


class TechnicalFocalPoint(models.Model):
    _name = 'technical.focal.point'
    _description = 'Description'

    name = fields.Char(
        string='Description',
        translate=True,
        require=True)
