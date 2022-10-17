from ssl import OP_NO_TLSv1_2
import string


class Student:
    def __init__(self, name):
        self._name = name

    def _str_(self):
        return f'Name: {self._name}'


class Library:
    def __init__(self, city, street, zip_code, open_hours, phone):
        self._city = city
        self._street = street
        self._zip_code = zip_code
        self._open_hours = open_hours
        self._phone = phone

    def _str_(self):
        return f'Biblioteka:\n{self._street}, {self._zip_code} {self._city}\n{self._phone}\n\n'

class Employee:
    def __init__(self, first_name, last_name, hire_date, birth_date, city, street, zip_code, phone):
        self._first_name = first_name
        self._last_name = last_name
        self._hire_date = hire_date
        self._birth_date = birth_date
        self._city = city
        self._street = street
        self._zip_code = zip_code
        self._phone = phone

    def _str_(self):
        return f'Pracownik:\n{self._first_name} {self._last_name}\n{self._phone}\n\n'

class Book:
    def __init__(self, library, publication_date, author_name, author_surname, number_of_pages):
        self._library = library
        self._publication_date = publication_date
        self._author_name = author_name
        self._author_surname = author_surname
        self._number_of_pages = number_of_pages


    def _str_(self):
        return f'Dane książki:\n{self._library._str_()}\n{self._publication_date}\n{self._author_name} {self._author_surname}\n\n'

class Order:
    def __init__(self, employee, student, books, order_date):
        self._employee = employee
        self._student = student
        self._books = string.Join(' ', books)
        self._order_date = order_date

    def _str_(self):
        return f'{self._employee._str_()} {self._student._str_()} {self._books._str_()} {self._order_date._str_()}'

s1 = Student("Adam Kowalski")
s2 = Student("Bartosz Kowalski")
s3 = Student("Michał Kowalski")

e1 = Employee("Adam", "Kowalski", "2020-10-10", "1990-10-10", "Katowice", "Mariacka", "43-120", 123456789)
e2 = Employee("Bartosz", "Kowalski", "2020-10-10", "1990-10-10", "Katowice", "Mariacka", "43-120", 123456789)
e3 = Employee("Michał", "Kowalski", "2020-10-10", "1990-10-10", "Katowice", "Mariacka", "43-120", 123456789) 

l1 = Library("Katowice", "Mariacka", "43-120", "8-20", 123456789)
l2 = Library("Katowice", "Mariacka", "43-120", "8-20", 123456789)

b1 = Book(l1, "2022-02-22", "Adam", "Mickiewicz", 50)
b2 = Book(l2, "2022-02-22", "Adam", "Mickiewicz", 50)
b3 = Book(l1, "2022-02-22", "Adam", "Mickiewicz", 50)
b4 = Book(l2, "2022-02-22", "Adam", "Mickiewicz", 50)
b5 = Book(l1, "2022-02-22", "Adam", "Mickiewicz", 50)

books1 = [b1, b2, b3]
books2 = [b4, b5]

o1 = Order(e1, s2, books1, "2022-10-17")
o2 = Order(e2, s1, books2, "2022-10-16")

print(o1._str_(), o1._str_())