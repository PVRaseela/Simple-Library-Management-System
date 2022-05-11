

class student:

    def __init__(self, stName):
        self.studentName = stName

    def registration(self):
        student = []
        if self.studentName not in student:
            student.append(self.studentName)
            print('student added to the list')
            print(student)


class SLibrary(student):

    def __init__(self, bookName, booklist):
        self.book = bookName
        self.lbooks = booklist

    def selectbooks(self):

        if self.book in self.lbooks:
            print(
                'Book ready for delivery..please collect from the desk and should be returned with in 30 days')
            self.lbooks.remove(self.book)
            self.manageBook()

        else:
            print("Book not available")

    def manageBook(self):
        bstring = ",".join(self.lbooks)
        file = open('books.txt', 'w')
        file.write(bstring)

        LibDict = dict()
        LibDict[StudentName] = self.book
        print(LibDict)


books = open('books.txt', 'r')
booklist = books.read().split(',')
print(booklist)

StudentName = input("Enter the Student Username : ")
BookName = input("Enter the Book Name to check Availability : ")
st = student(StudentName)
lib = SLibrary(BookName, booklist)
lib.selectbooks()
