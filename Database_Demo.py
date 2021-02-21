import sqlite3

#conn = sqlite3.connect("bookdata.db")
# Create table
Create_Table = """CREATE TABLE IF NOT EXISTS bookdata (BookId TEXT,BookName TEXT, Pages INTEGER,PRIMARY KEY("BookId"))"""
# Insert data (new book added)
#insert_book = "INSERT INTO bookdata VALUES ('1703','Hello world',50)"
insert_book = "INSERT INTO bookdata (BookId,BookName,Pages) VALUES (?,?,?);"
# show all data from table
show_all_books = "SELECT * FROM bookdata;"
# find book by id
find_book_by_id = "SELECT * FROM bookdata WHERE BookId=?"
# Delete Book
delete_book = "DELETE FROM bookdata WHERE BookId=?"
# Update Book details
update_book = "UPDATE bookdata SET BookName=?,Pages=? WHERE BookId=?"

def connet():
    return sqlite3.connect("bookdata.db")

def CreateTable(connection):
    with connection:
        connection.execute(Create_Table)

def BookInsert(connection,BookId,BookName,Pages):
    with connection:
        connection.execute(insert_book,(BookId,BookName,Pages))

def ShowAllBooks(connection):
    with connection:
        return connection.execute(show_all_books).fetchall()

def FindBookById(connection,BookId):
    with connection:
        return connection.execute(find_book_by_id,(BookId,)).fetchall()

def DeleteBook(connection,BookId):
    with connection:
        return connection.execute(delete_book,(BookId,))

def UpdateBook(connection,BookId,BookName,Pages):
    with connection:
        connection.execute(update_book,(BookId,BookName,Pages))
