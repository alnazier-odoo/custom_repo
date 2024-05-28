from odoo import fields, models, api


class AuctionsStages(models.Model):
    _name = 'auctions.stages'
    _description = 'Description'

    name = fields.Char(
        string='Stage Name',
        require=True)

    sequence = fields.Integer(
        string='Sequence'
    )