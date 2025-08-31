from odoo import api, fields, models, _


class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _description = 'Patient Master'
    name = fields.Char(string='Name', required=True)
    date_of_birth = fields.Datetime(string='DOB')
    gender = fields.Selection([("male", "Male"), ("female", "Female")], string='Gender')
