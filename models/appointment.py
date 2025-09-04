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
    state = fields.Selection([
        ("draft", "Draft"), ("confirmed", "Confirmed"), ("ongoing", "Ongoing"),
        ("done", "Done"), ("cancel", "Cancelled")
    ], default="draft", tracking=True)

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if not vals.get('mrn') or vals['mrn'] == "New Appointment":
                vals['mrn'] = self.env['ir.sequence'].next_by_code('hospital.appointment')
        return super().create(vals_list)

    def action_confirm(self):
        for rec in self:
            rec.state = "confirmed"

    def action_ongoing(self):
        for rec in self:
            rec.state = "ongoing"

    def action_done(self):
        for rec in self:
            rec.state = "done"

    def action_cancel(self):
        for rec in self:
            rec.state = "cancel"

    def action_reset_to_draft(self):
        for rec in self:
            rec.state = "draft"
