from odoo import fields, models, api,_


class Auctions(models.Model):
    _name = 'auctions.app'
    _description = 'Auctions'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(
        string='Name',
        translate=True,
        required=True, tracking=True)

    plant_location = fields.Char(
        string='Plant Location',
        copy=True,
        store=True,
        required=False, tracking=True)

    brief_description = fields.Text(
        string="Brief Description",
        required=False, tracking=True)

    partner_id = fields.Many2one(
        comodel_name='res.partner',
        string='Owner',
        copy=True,
        required=False, tracking=True)

    phone = fields.Char(
        string='Phone',
        store=True,
        required=False, tracking=True)

    partner_email = fields.Char(
        string='Email',
        store=True,
        required=False, tracking=True)

    last_day_for_site_visits = fields.Date(
        string='Last Day for Site Visits',
        required=False, tracking=True)

    last_day_to_submit_bids = fields.Date(
        string='Last Day to Submit Bids',
        copy=True,
        required=False, tracking=True)

    bids_open_date = fields.Date(
        string='Bids Open Date',
        copy=True,
        required=False, tracking=True)

    announce_bids_results = fields.Date(
        string='Announce Bids Results',
        copy=True,
        required=False, tracking=True)

    brief_description = fields.Text(
        string='Brief Description',
        copy=True,
        required=False, tracking=True)

    company_id = fields.Many2one(
        comodel_name='res.company',
        string='Company',
        required=False, tracking=True)

    color = fields.Integer(
        string='Color',
        required=False)

    # technical_point = fields.Many2one(
    #     comodel_name='auctions.app',
    #     string='Technical Focal Point',
    #     required=False, tracking=True)

    attachment = fields.Binary(
        string="Attachment",
        copy=True,)

    attachment_filename = fields.Char(
        string="Attachment Filename",
        copy=True,)

    notes = fields.Html(
        string="Notes",
        copy=True,
        store=True,
        required=False, tracking=True)

    user_id = fields.Many2one(
        comodel_name='res.users',
        string='Responsible',
        store=True,
        copy=True,
        required=False, tracking=True)

    active = fields.Boolean(
        string='Active',
        required=False)

    site_visits_count = fields.Integer(
        string='Auctions count',
        required=False)

    buyer_count = fields.Integer(
        string='Buyer Count',
        required=False)

    announce_bids_results = fields.Date(
        string=' Announce Bids Results',
        copy=True,
        required=False)

    buyer_id = fields.One2many(
        comodel_name='buyer.buyer',
        inverse_name='auctions_id',
        string=' Buyer Auction',
        required=False)

    company_stamp = fields.Binary(
        string="Company Stamp",
        store=True)

    employee_signature = fields.Binary(
        string="Employee Signature",
        store=True,)




    buyer_count = fields.Integer(
        string='Buyers',
        compute="_compute_buyer_count",
        required=False)

    kanban_state = fields.Selection(
        string='State',
        copy=True,
        selection=[
            ('normal', 'In Progress'),
            ('done', 'Ready'),
            ('blocked', 'Blocked'), ],
        required=False, )
    
    priority = fields.Boolean(
        string='Priority',
        store=True,
        copy=True,
        required=False)

    sequence = fields.Integer(
        string=' sequence',
        store=True,
        copy=True,
        required=False)

    site_manager = fields.Many2one(
        comodel_name='hr.employee',
        string='Site Manager',
        store=True,
        copy=True,
        required=False)

    stage_id = fields.Many2one(
        comodel_name='auctions.stages',
        string='Stage',
        store=True,
        copy=True,
        required=True)

    @api.depends("buyer_count")
    def _compute_buyer_count(self):
        for rec in self:
            result = self.env['buyer.buyer'].search_count([("auctions_id", "=", rec.name)])

            rec.buyer_count = result

    def buyer_count_action(self):
        return {
            "type": "ir.actions.act_window",
            "res_model": "buyer.buyer",
            "views": [[False, "tree"]],
            "domain": [("auctions_id", "=", self.name)],
            "name": _("Interesting Buyers"),
        }






