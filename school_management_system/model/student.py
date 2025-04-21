from odoo import models ,fields

class StudentDetail(models.Model):
    """
    Description: Student Class which is used to store student information
    """
    _name = "student.information" 
    _description = "This Model is used to store the information of the student "
    _inherit="common.details"

    roll_number = fields.Integer("Roll Number")
    branch = fields.Char("Branch")
    admission_date=fields.Date('Admission Date')
    leaving_date=fields.Date('leaving Date')
    section = fields.Selection([('A', 'A'), ('B', 'B'),('C','C'),('D','D')])
    teacher_id=fields.Many2one(comodel_name='teacher.information',string="class Teacher")
    
    def create(self, vals):
        """
        Description: Create a new student record.
        """

        if 'roll_number' in vals:
            existing_student = self.env['student.information'].search([('roll_number', '=', vals['roll_number'])])
            if existing_student:
                raise ValueError("Roll Number already exists.")
        return super(StudentDetail, self).create(vals)

    def write(self, vals):
        """
        Description: Update student records.
        """
        if 'age' in vals:
            vals['age'] = 21
        return super(StudentDetail, self).write(vals)

