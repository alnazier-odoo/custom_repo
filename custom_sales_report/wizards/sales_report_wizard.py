from odoo import fields, models, api, _


class SalesWizard(models.Model):
    _name = 'sales.report.wizards'
    _description = 'Sales Report Features'

    from_date = fields.Date(string='From Date', required=False)
    to_date = fields.Date(string='To Date', required=False)

    filter_by = fields.Selection(string='Filter By',
                                 selection=[('duration', 'Duration'),
                                            ('partner_id', 'Customer'),
                                            ('user_id', 'Salesperson')],
                                 required=False, )

    customer = fields.Many2many(comodel_name='res.partner', string='Customers')
    saleperson = fields.Many2many(comodel_name='res.users', string='Salesperson')

    def get_sales_person_report(self):
        sales_person = []
        for person in self.saleperson:
            per = {
                'name': person.name
            }
            sales_person.append(per)
        return sales_person

    def get_customer_report(self):
        customers = []
        for person in self.customer:
            per = {
                'name': person.name
            }
            customers.append(per)
        return customers

    def _get_data(self):
        if self.filter_by == 'partner_id':
            customers = self.customer
            result = []
            for customer in customers:
                sales = self.env['sale.order'].search([('partner_id', '=', customer.id)])
                for so in sales:
                    if self.from_date <= so.convert_date <= self.to_date:
                        for lines in so.order_line:
                            res = {
                                'sequence': so.name,
                                'date': so.convert_date,
                                'partner': so.partner_id.name,
                                'product': lines.product_template_id.name,
                                'quantity': lines.product_uom_qty,
                                'cost': lines.price_unit,
                                'subtotal': lines.price_subtotal,
                            }
                            result.append(res)

                datas = {
                    'ids': self,
                    'model': 'sales.report.wizards',
                    'form': result,
                    'person': self.get_customer_report(),
                    'start_date': self.from_date,
                    'end_date': self.to_date,
                    'filter_by': self.filter_by,

                }
                return datas

        if self.filter_by == 'user_id':
            users = self.saleperson
            result = []
            for person in users:
                sales = self.env['sale.order'].search([('user_id', '=', person.id)])
                for so in sales:
                    if self.from_date <= so.convert_date <= self.to_date:
                        for lines in so.order_line:
                            res = {
                                'sequence': so.name,
                                'date': so.convert_date,
                                'partner': so.partner_id.name,
                                'product': lines.product_template_id.name,
                                'quantity': lines.product_uom_qty,
                                'cost': lines.price_unit,
                                'subtotal': lines.price_subtotal,
                            }
                            result.append(res)

                datas = {
                    'ids': self,
                    'model': 'sales.report.wizards',
                    'form': result,
                    'person': self.get_sales_person_report(),
                    'start_date': self.from_date,
                    'end_date': self.to_date,
                    'filter_by': self.filter_by,

                }
                return datas

        if self.filter_by == 'duration':
            result = []
            sales = self.env['sale.order'].search([('state', '!=', 'cancel')])
            for so in sales:
                if self.from_date <= so.convert_date <= self.to_date:
                    for lines in so.order_line:
                        res = {
                            'sequence': so.name,
                            'date': so.convert_date,
                            'partner': so.partner_id.name,
                            'product': lines.product_template_id.name,
                            'quantity': lines.product_uom_qty,
                            'cost': lines.price_unit,
                            'subtotal': lines.price_subtotal,
                        }
                        result.append(res)

            datas = {
                'ids': self,
                'model': 'sales.report.wizards',
                'form': result,
                'person': self.get_sales_person_report(),
                'start_date': self.from_date,
                'end_date': self.to_date,
                'filter_by': self.filter_by,

            }
            return datas

    def print_report(self):
        datas = self._get_data()
        return self.env.ref('custom_sales_report.action_sales_report').report_action([], data=datas)
