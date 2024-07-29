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

rollno = int(input('Enter the roll no of the student: '))
name = input('Enter the name of the student: ')
marks = int(input('Enter  one subject marks: '))

add = addStudent(rollno, name, marks)
print(add)

