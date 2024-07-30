"""
Student Management System
"""
students = {'Student': []}

# Add Student function

def addStudent(rno, nm, m):
    student = {'RollNumber': rno,
               'Name': nm,
               'Marks': m}
    students['Student'].append(student)
    return students

