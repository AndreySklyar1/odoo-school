import logging

from odoo import models, fields

_loger = logging.getLogger(__name__)

class patient_card(models.Model):
    _name = 'hr_hospital.card_patient'
    _description = 'card patient'

    name = fields.Char()
    active = fields.Boolean(default=True, )
    # isbn = fields.Char()
