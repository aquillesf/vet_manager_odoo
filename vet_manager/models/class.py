from odoo import models, fields

class  AnimalClass(models.Model):
    _name = "animal.class"
    _description = "Animal Class"

    name =  fields.char(string = "Name")