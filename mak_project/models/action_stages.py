from odoo import api, fields, models


class ProjectActionStages(models.Model):
    _name = "project.action_stages"
    # _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Project Action Stages"

    stage_name = fields.Text(string="Stage Name")
