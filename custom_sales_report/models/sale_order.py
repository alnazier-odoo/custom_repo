from odoo import fields, models, api, _


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    convert_date = fields.Date(
        string='Convert Date',
        compute='get_convert_date',
        required=False)

    @api.depends('date_order')
    def get_convert_date(self):
        for rec in self:
            rec.convert_date = rec.date_order.date()



