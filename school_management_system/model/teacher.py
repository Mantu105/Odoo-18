from odoo import models ,fields

class TeacherDetail(models.Model):
    _name = "teacher.information"
    _description = "This model is used to store the information of the teacher"
    _inherit = 'common.details'
    
    subject = fields.Char("Subject")
    salary=fields.Integer("Salary")
