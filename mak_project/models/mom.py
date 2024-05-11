from odoo import api, fields, models, _


class ProjectMom(models.Model):
    _name = "project.mom"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Project Mom"
    _rec_name = "meeting_reference"

    reference = fields.Char(string="ref", copy=False, required=True, default=lambda self: _('New'))
    meeting_reference = fields.Char(string='Meeting Reference', tracking=True)
    meeting_date = fields.Date(string="Meeting Date", tracking=True)
    time = fields.Char(string="Time", tracking=True)
    location = fields.Char(string='Location', tracking=True)
    task = fields.Many2one('project.task', string="Task", tracking=True)
    project = fields.Many2one('project.project', string="Project", tracking=True)
    company = fields.Many2one('res.company', string="Company", tracking=True)
    agenda = fields.Text(string="Agenda", tracking=True)
    discussion_summary = fields.Text(string="Discussion Summary", tracking=True)
    attendees = fields.Many2many('res.partner', string="Attendees", tracking=True)
    action_items_ids = fields.One2many('project.items', 'mom', string="Action Items")

    @api.model
    def create(self, vals):
        if not vals.get('discussion_summary'):
            vals['discussion_summary'] = 'New Reference'
        if vals.get('reference', _('New')) == _('New'):
            vals['reference'] = self.env['ir.sequence'].next_by_code('project.mom') or _('New')
        res = super(ProjectMom, self).create(vals)
        return res


