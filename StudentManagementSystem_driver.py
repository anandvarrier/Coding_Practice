from StudentManagementSystem import addStudent, searchStudent
#delStudent, updateStudent, exitStudent

while True:
    opt = int(input('Enter option\n 1.Add Student\n 2.Search Student\n 3.Delete Student\n 4.Update Student\n 5.Exit\n Your Choice: '))
    if opt == 1:
        n = int(input('Enter the number of students: '))
        for _ in range(n):
            rollno = int(input('Enter the roll no of the student: '))
            name = input('Enter the name of the student: ')
            marks = int(input('Enter  one subject marks: '))
            add = addStudent(rollno, name, marks)
        print(add)
        opt
    elif opt == 2:
        search_rno = int(input('Enter the roll number you want to search: '))
        search = searchStudent(search_rno)
    elif opt == 3:
        delete = delStudent()
    elif opt == 4:
        update == updateStudent()
    elif opt == 5:
        exit_sys = exitStudent()
    else:
        print('Please enter a correct option')
