from odoo import fields, models, api, _


class PurchaseWizard(models.Model):
    _name = 'purchase.report.wizards.ah'
    _description = 'Purchase Report Features'

    from_date = fields.Date(
        string='From Date',
        required=False)
    to_date = fields.Date(
        string='To Date',
        required=False)

    partner_ids = fields.Many2many(
        comodel_name='res.users',
        string='Purchase Representatives ')

    suppliers = fields.Many2many(
        comodel_name='res.partner',
        string='Supplier')

    filter_by = fields.Selection(
        string='Filter By',
        selection=[('duration', 'Duration'),
                   ('vendor', 'Supplier'), ('partner', 'Purchase Representatives')],
        required=False, )

    def get_person_report(self):
        persons = []
        for person in self.partner_ids:
            per = {
                'name': person.name
            }
            persons.append(per)
        return persons

    def get_supplier_report(self):
        supplier = []
        for person in self.suppliers:
            per = {
                'name': person.name
            }
            supplier.append(per)
        return supplier

    def _get_data(self):
        if self.filter_by == 'vendor':
            vendors = self.suppliers
            result = []
            for vendor in vendors:
                purchase = self.env['purchase.order'].search(
                    [('partner_id', '=', vendor.id)])
                for so in purchase:
                    if self.from_date <= so.convert_date <= self.to_date:
                        for lines in so.order_line:
                            res = {
                                'sequence': so.name,
                                'date': so.convert_date,
                                'partner': so.partner_id.name,
                                'partner_ref': so.partner_ref,
                                'product_code': lines.product_id.default_code,
                                'product': lines.product_id.name,
                                'quantity': lines.product_uom_qty,
                                'cost': lines.price_unit,
                                'subtotal': lines.price_subtotal,
                                'vendor': vendor.name,
                            }
                            result.append(res)

            datas = {
                'ids': self,
                'model': 'purchase.report.wizards.ah',
                'form': result,
                'person': self.get_supplier_report(),
                'start_date': self.from_date,
                'end_date': self.to_date,
                'filter_by': self.filter_by,

            }
            return datas

        if self.filter_by == 'partner':
            vendors = self.partner_ids
            result = []
            for vendor in vendors:
                purchase = self.env['purchase.order'].search(
                    [('user_id', '=', vendor.id), ])
                for so in purchase:
                    if self.from_date <= so.convert_date <= self.to_date:
                        for lines in so.order_line:
                            res = {
                                'sequence': so.name,
                                'date': so.convert_date,
                                'partner': so.partner_id.name,
                                'partner_ref': so.partner_ref,
                                'product_code': lines.product_id.default_code,
                                'product': lines.product_id.name,
                                'quantity': lines.product_uom_qty,
                                'cost': lines.price_unit,
                                'subtotal': lines.price_subtotal,
                                'vendor': vendor.name,
                            }
                            result.append(res)
            datas = {
                'ids': self,
                'model': 'purchase.report.wizards.ah',
                'form': result,
                'person': self.get_person_report(),
                'start_date': self.from_date,
                'end_date': self.to_date,
                'filter_by': self.filter_by,

            }
            return datas
        if self.filter_by == 'duration':
            result = []
            purchase = self.env['purchase.order'].search([('state', '!=', 'cancel')])
            for so in purchase:
                if so.convert_date >= self.from_date and so.convert_date <= self.to_date:
                    for lines in so.order_line:
                        res = {
                            'sequence': so.name,
                            'date': so.convert_date,
                            'vendor': so.partner_id.name,
                            'partner': so.user_id.name,
                            'partner_ref': so.partner_ref,
                            'product_code': lines.product_id.default_code,
                            'product': lines.product_id.name,
                            'quantity': lines.product_uom_qty,
                            'cost': lines.price_unit,
                            'subtotal': lines.price_subtotal,
                        }
                        result.append(res)

            datas = {
                'ids': self,
                'model': 'purchase.report.wizards.ah',
                'form': result,
                'person': self.get_person_report(),
                'start_date': self.from_date,
                'end_date': self.to_date,
                'filter_by': self.filter_by,

            }
            return datas

    def print_report(self):
        datas = self._get_data()
        return self.env.ref('custom_purchase_wizard.action_ah_purchase_report').report_action([], data=datas)
