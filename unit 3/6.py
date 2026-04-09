# 6) Write a Python Program that creates a class and inherit into another class (Base Class : Student with rollno, name, gender, age) (Derived Class : Course with coursename, duration, fee) 

# Base Class
class Student:
    def __init__(self, rollno, name, gender, age):
        self.rollno = rollno
        self.name = name
        self.gender = gender
        self.age = age

    def display_student(self):
        print("Roll No:", self.rollno)
        print("Name:", self.name)
        print("Gender:", self.gender)
        print("Age:", self.age)


# Derived Class
class Course(Student):
    def __init__(self, rollno, name, gender, age, coursename, duration, fee):
        super().__init__(rollno, name, gender, age)
        self.coursename = coursename
        self.duration = duration
        self.fee = fee

    def display_course(self):
        self.display_student()
        print("Course Name:", self.coursename)
        print("Duration:", self.duration)
        print("Fee:", self.fee)


# Object creation
c = Course(101, "Nevil", "Male", 20, "Python", "6 Months", 15000)
c.display_course()