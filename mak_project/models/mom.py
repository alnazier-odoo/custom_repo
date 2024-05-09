from odoo import api, fields, models, _


class ProjectMom(models.Model):
    _name = "project.mom"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Project Mom"

    meeting_reference = fields.Char(string='Meeting Reference', translate=True, tracking=True)
    meeting_date = fields.Date(string="Meeting Date")
    time = fields.Char(string="Time")
    location = fields.Char(string='Location', tracking=True)
    task = fields.Many2one('project.task', string="Task")
    project = fields.Many2one('project.project', string="Project")
    company = fields.Many2one('res.company', string="Company")
    agenda = fields.Text(string="Agenda")
    discussion_summary = fields.Text(string="Discussion Summary")
    attendees = fields.Many2many('res.partner', string="Attendees")
