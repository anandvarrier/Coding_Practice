from StudentManagementSystem import addStudent, searchStudent, delStudent, updateStudent

while True:
    opt = int(input('Enter option\n 1.Add Student\n 2.Search Student\n 3.Delete Student\n 4.Update Student\n 5.Exit\n Your Choice: '))
    if opt == 1:
        n = int(input('Enter the number of students: '))
        for _ in range(n):
            rollno = int(input('Enter the roll no of the student: '))
            name = input('Enter the name of the student: ')
            marks = int(input('Enter one subject marks: '))
            add_result = addStudent(rollno, name, marks)
        print(add_result)
    elif opt == 2:
        search_rno = int(input('Enter the roll number you want to search: '))
        result = searchStudent(search_rno)
        if result:
            print(f"Student found: {result}")
        else:
            print("Student not found")
    elif opt == 3:
        delete_rno = int(input('Enter the roll number you want to delete: '))
        result = delStudent(delete_rno)
        if result:
            print(result)
        else:
            print("Student not found")
    elif opt == 4:
        rollno = int(input('Enter the roll number you want to update: '))
        name = input('Enter the new name of the student: ')
        marks = int(input('Enter the new marks: '))
        result = updateStudent(rollno, name, marks)
        if result:
            print(result)
        else:
            print("Student not found")
    elif opt == 5:
        print('Successfully Exiting.')
        break
    else:
        print('Please enter a correct option')
