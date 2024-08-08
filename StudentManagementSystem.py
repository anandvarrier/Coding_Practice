"""
Student Management System
"""
students = {}

# Add Student function
def addStudent(rno, nm, m):
    students[rno] = {'Name': nm, 'Marks': m}
    return students

# Search Student function
def searchStudent(rollno):
    return students.get(rollno, None)

# Delete Student function
def delStudent(rollno):
    if rollno in students:
        del students[rollno]
        return f"Student with roll number {rollno} has been deleted"
    return None

# Update Student function
def updateStudent(rno, nm, m):
    if rno in students:
        students[rno] = {'Name': nm, 'Marks': m}
        return f"Student with roll number {rno} has been updated"
    return None
