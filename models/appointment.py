from odoo import api, fields, models, _


class HospitalAppointment(models.Model):
    _name = 'hospital.appointment'
    _inherit = ['mail.thread']
    _description = 'Hospital Appointment'
    _rec_name = 'patient_id'

    mrn = fields.Char('Medical Record Number', default="New Appointment")
    patient_id = fields.Many2one('hospital.patient', string="Patient", tracking=True)
    date_appointment = fields.Date(string="Date", tracking=True)
    note = fields.Text(string="Notes", tracking=True)

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if not vals.get('mrn') or vals['mrn'] == "New Appointment":
                vals['mrn'] = self.env['ir.sequence'].next_by_code('hospital.appointment')
        return super().create(vals_list)
