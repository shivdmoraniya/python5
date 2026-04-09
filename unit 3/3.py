# 3) Write a program to make use of class method and instance method. 

class Student:
    school = "ABC School"

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print("Name:", self.name)
        print("Marks:", self.marks)

    @classmethod
    def showSchool(cls):
        print("School Name:", cls.school)


s1 = Student("Natho", 85)

s1.display()

Student.showSchool()