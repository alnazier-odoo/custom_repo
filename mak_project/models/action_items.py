from odoo import api, fields, models, _


class ProjectActionItems(models.Model):
    _name = "project.items"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Project Action Items"

    sequence = fields.Char(string="Seq", copy=False, required=True, default=lambda self: _('New'))
    name = fields.Char(string="Name", required=True, tracking=True)
    due_date = fields.Date(string="Due Date", required=True, tracking=True)
    project = fields.Many2one('project.project', string="Project", required=True, tracking=True)
    task = fields.Many2one('project.task', string="Task", required=True, tracking=True)
    mom = fields.Many2one('project.mom', string="Mom", required=True, tracking=True)
    company = fields.Many2one('res.company', string="Company", required=True, tracking=True)
    remark = fields.Text(string="Remark", tracking=True)
    description = fields.Text(string="Description", tracking=True)
    action_party = fields.Many2many('project.tag', string="Action Party", required=True, tracking=True)

    @api.model
    def create(self, vals):
        if not vals.get('remark'):
            vals['remark'] = 'New Item'
        if vals.get('sequence', _('New')) == _('New'):
            vals['sequence'] = self.env['ir.sequence'].next_by_code('project.items') or _('New')
        res = super(ProjectActionItems, self).create(vals)
        return res
