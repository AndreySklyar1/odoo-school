import logging

from odoo import fields, models

_loger = logging.getLogger(__name__)


class card_patient(models.Model):
    _name = 'hr_hospital.card_patient'
    _description = 'card patient'

    name = fields.Char()
    active = fields.Boolean(default=True, )
    isbn = fields.Char()

    diagnosis_ids = fields.Many2many(
        comodel_name='hr_hospital.diagnosis', )

    doctor_ids = fields.Many2many(
        comodel_name='hr_hospital.doctor', )
