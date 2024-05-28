from odoo import fields, models, api


class SalesFocalPoint(models.Model):
    _name = 'sales.focal.point'
    _description = 'sales_focal_point'

    name = fields.Char(
        string='Description',
        translate=True,
        require=True)