from odoo import api, fields, models


class ProjectActionStages(models.Model):
    _name = "project.stages"
    _description = "Project Action Stages"

    stage_name = fields.Text(string="Stage Name")
