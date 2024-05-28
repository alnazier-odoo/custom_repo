from odoo import fields, models, api


class VisitsStages(models.Model):
    _name = 'visits.stages'
    _description = 'Description'

    name = fields.Char(
        require=True,
    )

    sequence = fields.Integer(
        string='Sequence',
        required=False)
