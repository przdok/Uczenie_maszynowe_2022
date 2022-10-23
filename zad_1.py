class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def is_passed(self):
        if self.marks > 50:
            return True
        else:
            return False


s1 = Student("Maria", 51)
s2 = Student("Andrzej", 49)
print(f"Czy {s1.name} zdała? {s1.is_passed()}")
print(f"Czy {s2.name} zdała? {s2.is_passed()}")
