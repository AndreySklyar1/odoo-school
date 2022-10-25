import logging

from odoo import models, fields

_loger = logging.getLogger(__name__)


class patient(models.Model):
    _name = 'hr_hospital.patient'
    _description = 'patient'

    name = fields.Char()
    active = fields.Boolean(default=True, )
    isbn = fields.Char()