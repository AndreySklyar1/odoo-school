import logging

from odoo import fields, models

_loger = logging.getLogger(__name__)


class patient(models.Model):
    _name = 'hr_hospital.patient'
    _description = 'patient'

    name = fields.Char()
    active = fields.Boolean(default=True, )
    isbn = fields.Char()

    card_patient_ids = fields.Many2many(
        comodel_name='hr_hospital.card_patient',)
