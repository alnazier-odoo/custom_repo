from odoo import api, fields, models, _


class ProjectActionItems(models.Model):
    _name = "project.items"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Project Action Items"

    due_date = fields.Date(string="Due Date")
    project = fields.Many2one('project.project', string="Project")
    task = fields.Many2one('project.task', string="Task")
    mom = fields.Many2one('project.mom', string="Mom")
    company = fields.Many2one('res.company', string="Company")
    remark = fields.Text(string="Remark")
    description = fields.Text(string="Description")
    action_party = fields.Many2many('project.tag', string="Action Party")
    sequence = fields.Integer(string="Seq")
