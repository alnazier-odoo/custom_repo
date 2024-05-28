from odoo import fields, models, api


class BuyerBuyer(models.Model):
    _name = 'buyer.buyer'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(
        readonly=True,
        compute="_compute_contact_name",
                       )

    buyer = fields.Many2one(
        comodel_name='buyer.database',
        string='Buyer',
        required=False)
    
    sale_focal_point = fields.Many2one(
        comodel_name='buyer.database',
        string='Sale Focal Point',
        required=False)
    
    participated = fields.Selection(
        string='Participated',
        selection=[('participated_in_bid', 'Participated In Bid'),
                   ('did_participated_in_bid', 'Didn`t Participated In Bid '), ],
        required=False, )
    
    technical_evaluation = fields.Selection(
        string='Technical_evaluation',
        selection=[('pass', 'Pass'),
                   ('not_pass', 'Not Pass'), ],
        required=False, )

    auctions_id = fields.Many2one(
        comodel_name='auctions.app',
        string=' Auctions',
        required=False, tracking=True)

    technical_focal_point = fields.Char(
        string='Sale Focal Point',
        required=False)

    priority = fields.Selection(
        string='Priority',
        selection=[('a', 'A'),
                   ('b', 'B'),
                   ('c', 'C'),
                   ('d', 'D'),
                   ('x', 'X'), ],
        required=False, )

    meeting_status = fields.Selection(
        string='Meeting Status',
        selection=[('requested', 'Requested'),
                   ('scheduled', 'Scheduled'),
                   ('done', 'Done'), ],
        required=False, )

    category = fields.Selection(
        string='Category',
        selection=[('Buying', 'Buying'),
                   ('Demolishing', 'Demolishing'),
                   ('Buying/Demolishing', 'Buying/Demolishing'),
                   ('Recycling', 'Recycling'), ],
        required=False, )

    re_usescrap = fields.Selection(
        string='Re-Use/Scrap',
        selection=[('Re-Use', 'Re-Use'),
                   ('Scrap', 'Scrap'),
                   ('Re-Use/Scrap', 'Re-Use/Scrap'), ],
        required=False, )
    
    location = fields.Char(
        string='Location', 
        reafonly=True,
        required=False)

    remark = fields.Text(
        string="Remark",
        required=False)

    state = fields.Selection(
        string='State',
        copy=True,
        selection=[
            ('normal', 'In Progress'),
            ('done', 'Ready'),
            ('blocked', 'Blocked'), ],
        required=False, )

    @api.depends('buyer')
    def _compute_contact_name(self):
        for rec in self:
            if rec.buyer:
                if rec.auctions_id:
                    rec.name = "('" + rec.buyer.name +"','"+ rec.auctions_id.name + "')"
                else:
                    rec.name = "('" + rec.buyer.name + "','" + "false')"
            else:
                rec.name = "(false,false)"








        
        
        
        
