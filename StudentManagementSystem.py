"""
Student Management System
"""
students = {}

# Add Student function
def addStudent(rno, nm, m):
    student = {'RollNumber': rno,
               'Name': nm,
               'Marks': m}
    students = dict(student)
    return students

# Search Student
def searchStudent(rollno):
    for i in range(len(students)):
        if students[i]['RollNumber'] == rollno:
            print('Hi')


