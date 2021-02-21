from BookEntryApp import Database_Demo

Menu_List = """___Welcome to Book App___
Please Choose one of these option
1) Add New Book
2) Print All Books
3) Find book by book Id
4) Delete a Book
5) Update Your Book Details without Book ID
0) Exit
"""
def MenuList():
    connection = Database_Demo.connet()
    Database_Demo.CreateTable(connection)


    while True:
        print(Menu_List)
        response = int(input("Please select your option: "))
        if response==1:
            BookId = input("Create Book ID(Book id will be unique): ")
            BookName = input("Name of the Book: ")
            Pages = int(input("How much pages of your book? Type here: "))
            Database_Demo.BookInsert(connection,BookId,BookName,Pages)
            print(f"Successfully Your Book Id:{BookId}, Book Name:{BookName} and Book Pages:{Pages} Added")

        elif response==2:
            allbooks = Database_Demo.ShowAllBooks(connection)
            for show in allbooks:
                print(show)
        elif response==3:
            BookId = input("Enter Book Id: ")
            findbook = Database_Demo.FindBookById(connection,BookId)
            for fb in findbook:
                print(fb)
        elif response==4:
            BookId = input("Enter Book Id: ")
            deletebook = Database_Demo.DeleteBook(connection,BookId)
            print(f"This Book Deleted from the List. Your Book id is {BookId}")
        elif response==5:
            BookId = input("Enter Book Id: ")
            BookName = input("New Name of the book: ")
            Pages = input("New pages of the book: ")

            updatebook = Database_Demo.UpdateBook(connection,BookId,BookName,Pages)
            print(f"This book id {BookId} successfully added")
        else:
            print("Good luck reading")
            break

MenuList()
