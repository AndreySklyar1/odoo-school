import logging

from odoo import fields, models

_loger = logging.getLogger(__name__)


class doctor(models.Model):
    _name = 'hr_hospital.doctor'
    _description = 'doctor'

    name = fields.Char()
    active = fields.Boolean(default=True, )
    isbn = fields.Char()
