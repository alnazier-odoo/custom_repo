from odoo import api, fields, models, _


class ProjectActionTag(models.Model):
    _name = "project.tag"
    _description = "Project Action Tag"

    name = fields.Char(string="Name")
    color = fields.Integer(string="Color")
