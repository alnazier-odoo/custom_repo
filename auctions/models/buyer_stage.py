from odoo import fields, models, api


class BuyerStages(models.Model):
    _name = 'buyer.stages'
    _description = 'Description'

    name = fields.Char(
        require=True,
    )

    sequence = fields.Integer(
        string='Sequence')
