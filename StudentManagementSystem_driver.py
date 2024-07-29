from StudentManagementSystem import addStudent


n = int(input('Enter the number of students: '))

#options
"""
1. Add Student
2. Search Student
3. Delete Student
4. Update Student
"""

opt = int(input('Enter option\n 1.Add Student\n 2.Search Student\n 3.Delete Student\n 4.Update Student'))

if opt == 1:
    for _ in range(n+1):
        add = addStudent(roll, name, marks)
elif opt == 2:
    search = searchStudent()
elif opt == 3:
    delete = delStudent()
elif opt == 4:
    update == updateStudent()
else:
    print('Please enter a correct option')
