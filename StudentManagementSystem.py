"""
Student Management System
"""
students = {}

# Add Student function
def addStudent(rno, nm, m):
    students = {'Rollno': rno,
                'Details': {'Name': nm,
                            'Marks': m}}
    return students

# Search Student function
def searchStudent(rollno):
    for i in range(len(students)):
        if students[i]['RollNumber'] == rollno:
            print()


