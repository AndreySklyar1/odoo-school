import logging

from odoo import fields, models

_loger = logging.getLogger(__name__)


class diagnosis(models.Model):
    _name = 'hr_hospital.diagnosis'
    _description = 'diagnosis'

    name = fields.Char()
    active = fields.Boolean(default=True, )
    isbn = fields.Char()
