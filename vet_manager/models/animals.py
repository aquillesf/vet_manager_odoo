from odoo import models, fields, api

class ResAnimal(models.Model):
    _name = "res.animal"
    _description = "Animal"


    name = fields.Char(string="Name")
    birthday = fields.Date(string="Birthday")
    age = fields.Integer(string="Age", compute="compute_age")
    register_date = fields.Date(
        string="Register Date",
        default = fields.Date.context_today,
        readonly=True,
    )
    partner_id = fields.Many2one(comodel_name="res.partner", string="Tutor", required=True)
    class_id = fields.Many2one(comodel_name="animal.class", string="Class")
    species_id = fields.Many2one(comodel_name="animal.species", string="Species")
    breed_id = fields.Many2one(comodel_name="animal.breed", string="Breed")


    def compute_age(self):
        for item in self:
            if self.birthday:
                self.age = int((fields.Date.today() - self.birthday).days / 365)
            else:
                self.age= 0
