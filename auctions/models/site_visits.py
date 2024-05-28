from odoo import fields, models, api


class SiteVisit(models.Model):
    _name = 'site.visits'
    _description = 'Description'
    _inherit = ['mail.thread', 'mail.activity.mixin']


    name = fields.Char()

    buyer_id = fields.Many2one(
       comodel_name='buyer.buyer',
       string='Buyer Name',
       required=False)

    visit_date = fields.Date(
        string='Visit Date',
        required=True)

    visit_status = fields.Many2one(
        comodel_name='visits.status',
        string='Visit Status',
        required=False)

    gate_pass = fields.Char(
        string='Gate Pass Number',
        required=False)

    issuance_date = fields.Date(
        string='Issuance Date',
        required=False)

    request_date = fields.Date(
        string='Request Date',
        required=False)

    auctions_id = fields.Many2one(
        comodel_name='auctions.app',
        string='Auctions',
        required=False)

    company_id = fields.Char(
        related='auctions_id.company_id.name',
        string='Company',
        required=False)
    
    sale_focal_point = fields.Char(
        string='Sale Focal Point',
        required=False)

    technical_focal_point = fields.Char(
        string='Technical Focal Point',
        required=False)

    vehicle_type = fields.Char(
        string='Vehicle Type',
        required=False)

    plate_number = fields.Char(
        string='Plate Number',
        required=False)

    vehicle_file = fields.Binary(string="Vehicle File",)

    vehicle_file_filename = fields.Char(
        string=' vehicle_file_filename', 
        required=False)

    device_type = fields.Char(
        string='Device Type',
        required=False)

    device_brand = fields.Char(
        string='Device Brand',
        required=False)

    serial_number = fields.Char(
        string='Serial Number',
        required=False)

    device_file = fields.Binary(string="Device File")

    devices_file_filename = fields.Char(
        string='devices_file_filename',
        required=False)

    site_visit_line = fields.One2many(
        comodel_name='site.visits.line',
        inverse_name='site_visits_id',
        string='Site Visit Line',
        required=False)

    kanban_state = fields.Selection(
        string='State',
        selection=[('normal', 'In Progress'),
                   ('done', 'Ready'),
                   ('blocked', 'Blocked'), ],
        required=False, )

    stage_id = fields.Many2one(
        comodel_name='visits.stages',
        string='Stage',
        store=True,
        copy=True,
        required=True)

    class SiteVisitsLine(models.Model):
        _name = 'site.visits.line'

        name = fields.Char(
            string="Name",
            translate=True,
            require=True)

        # id_type = fields.Many2one(
        #     comodel_name='id.type',
        #     string='ID Type',
        #     required=False)

        id_number = fields.Char(
            string='ID Number',
            required=False)

        mobile_number = fields.Char(
            string='Mobile Number',
            required=False)

        nationality = fields.Many2one(
            comodel_name='res.country',
            string='Nationality',
            required=False)

        visit_status = fields.Selection(
            string='Visits Status',
            selection=[('requested', 'Requested'),
                       ('scheduled', 'Scheduled'),
                       ('re_scheduled', 'Re-Scheduled'),
                       ('completed', 'Completed'),
                       ('not_completed', 'Not Completed'), ],
            required=False, )

        remark = fields.Text(
            string="Remark",
            required=False)

        sequence = fields.Integer(
            string='Sequence',
            required=False)

        site_visits_id = fields.Many2one(
            comodel_name='site.visits',
            string='Site Visits Id',
            required=False)

            


