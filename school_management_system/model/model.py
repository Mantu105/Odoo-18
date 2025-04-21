#Importing the odoo Basic Modules
from odoo import models, fields

class CommonDetails(models.AbstractModel):
    _name = "common.details"
    _description = "Contain Common Informations"
    
    name = fields.Char("Name")
    age = fields.Integer("Age")
    date_of_birth = fields.Date("Date of Birth")
    profile_pic = fields.Image("Image")

