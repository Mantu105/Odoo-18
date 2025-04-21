{
    'name': "School Management System",
    'version': '18.0',
    'depends': ['base'],
    'author': "Manu Raj",
    'category': 'Management',
    'description': """
    This is the custom school model contain teacher and student information 
    """,
    'data': [
        'security/student_rules.xml',
        'security/ir.model.access.csv',

        'data/student.xml',
        'data/student.information.csv',

        'views/student_views.xml', 
        'views/teacher_views.xml',
    ],
    'license':'LGPL-3',
    'installable':True,
    'application':True,
}
