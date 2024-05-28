from odoo import fields, models, api


class VisitsStatus(models.Model):
    _name = 'visits.status'
    _description = 'Description'

    name = fields.Char()

    sequence = fields.Integer(
        string='Sequence',
        required=False)

    active = fields.Boolean(
        string='Active',
        required=False)

    status_color = fields.Integer(
        string='Status Color',
        required=False)
