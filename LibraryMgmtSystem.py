"""
This program is a Library Management System Code

Functions:
Add Books
View Books
Update Books
Delete Books
"""

class Books:
    def __init__(self, bId, bName, bAuthor, bPublisher):
        self.bId = bId
        self.bName = bName
        self.bAuthor = bAuthor
        self.bPublisher = bPublisher

    def __str__(self):
        return f"ID: {self.bId}, Name: {self.bName}, Author: {self.bAuthor}, Publisher: {self.bPublisher}"

# Global dictionary to store books
library = {}

def addBook():
    bId = int(input("Enter Book ID: "))
    bName = input("Enter Book Name: ")
    bAuthor = input("Enter Book Author: ")
    bPublisher = input("Enter Book Publisher: ")
    book = Books(bId, bName, bAuthor, bPublisher)
    library[bId] = book
    print(f"Book '{bName}' added successfully!\n")

def viewBooks():
    if not library:
        print("No books in the library.")
    else:
        for book in library.values():
            print(book)

def updateBook():
    bId = int(input("Enter Book ID to update: "))
    if bId in library:
        bName = input("Enter new Book Name: ")
        bAuthor = input("Enter new Book Author: ")
        bPublisher = input("Enter new Book Publisher: ")
        library[bId].bName = bName
        library[bId].bAuthor = bAuthor
        library[bId].bPublisher = bPublisher
        print("Book details updated successfully!\n")
    else:
        print("Book ID not found.")

def deleteBook():
    bId = int(input("Enter Book ID to delete: "))
    if bId in library:
        del library[bId]
        print("Book deleted successfully!\n")
    else:
        print("Book ID not found.")

if __name__ == "__main__":
    while True:
        print('Welcome to the Library Management System!\n')
        print('1) Add Books\n2) View Library\n3) Update Details\n4) Delete\n5) Exit')
        user_input = int(input('What would you like to do: \n'))

        if user_input == 1:
            addBook()
        elif user_input == 2:
            viewBooks()
        elif user_input == 3:
            updateBook()
        elif user_input == 4:
            deleteBook()
        elif user_input == 5:
            print("Exiting Library Management System.")
            break
        else:
            print("Invalid option. Please try again.")
