from odoo import fields, models, api, _


class BuyerDatabase(models.Model):
    _name = 'buyer.database'
    _description = 'Description'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = "name"

    sequence = fields.Integer(
        string=' sequence',
        required=False)

    name = fields.Char(
        string='Description',
        compute="_compute_contact_name",
        store=True,
        required=False)

    auctions_id = fields.Many2one(
        comodel_name='auctions.app',
        string=' Auctions',
        required=False, tracking=True)

    partner_id = fields.Many2one(
        comodel_name='res.partner',
        string='Contact',
        required=False, tracking=True)

    phone = fields.Char(
        string='Phone',
        related='partner_id.phone',
        required=False)

    partner_email = fields.Char(
        string='Email',
        related='partner_id.email',
        required=False)

    company_id = fields.Many2one(
        comodel_name='res.company',
        string='Company',
        store=True,
        required=False)

    user_id = fields.Many2one(
        comodel_name='res.users',
        string='User id',
        required=False)

    note = fields.Char(
        string='Note',
        required=False, tracking=True)

    participation_auctions_ids = fields.One2many(
        comodel_name='buyer.database.line',
        inverse_name='buyer_id',
        string='Participation in the Auctions',
        required=False, tracking=True)

    @api.depends('partner_id')
    def _compute_contact_name(self):
        for rec in self:
            if rec.partner_id:
              rec.name = rec.partner_id.name
            else:
                rec.name = ""







class BuyerDatabaseLine(models.Model):
    _name = 'buyer.database.line'
    _description = 'BuyerDatabaseLine'

    name = fields.Char(
        string='Name',
        required=False)

    buyer_id = fields.Many2one(
        comodel_name='buyer.database',
        string=' Buyer ID',
        required=False, tracking=True)

    interested = fields.Selection(
        string='Interested?',
        selection=[('interested', 'Interested?'),
                   ('not interested', 'Not Interested'), ],
        required=False, tracking=True)

    participated = fields.Selection(
        string='Participated?',
        selection=[('participated in bid', 'Participated in Bid'),
                   ('not participated in bid', 'Not Participated in Bid'), ],
        required=False, tracking=True)

    called = fields.Char(
        string='Called By',
        required=False, tracking=True)

    remark = fields.Text(
        string="Remark",
        required=False, tracking=True)

    sequence = fields.Integer(
        string='Sequence',
        required=False)





