class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def show_info(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Course:", self.course)


student1 = Student("Nika", 20, "Python")
student2 = Student("Mariam", 21, "Java")

print("Student 1:")
print(student1.name)
print(student1.age)
print(student1.course)
student1.show_info()

print()

print("Student 2:")
print(student2.name)
print(student2.age)
print(student2.course)
student2.show_info()


# Book
class Book:
    def __init__(self, title, author, year, genre):
        self.title = title
        self.author = author
        self.year = year
        self.genre = genre

    def show_info(self):
        print("Title:", self.title)
        print("Author:", self.author)
        print("Year:", self.year)
        print("Genre:", self.genre)

    def __str__(self):
        return "Book: " + self.title + ", Author: " + self.author + ", Year: " + str(self.year) + ", Genre: " + self.genre


book1 = Book("Harry Potter", "J.K. Rowling", 1997, "Fantasy")
book2 = Book("1984", "George Orwell", 1949, "Novel")

print()

print("Book 1:")
book1.show_info()

print()

print("Book 2:")
book2.show_info()

print()

print(book1)
print(book2)