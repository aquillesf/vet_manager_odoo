from odoo import models, fields

class AnimalBreed(models.Model):
    _name = "animal.breed"
    _description = "Animal Breed"

    name =  fields.char(string = "Name")
    class_id = fields.Many2one(comodel_name = "animal.species", string= "Species")
