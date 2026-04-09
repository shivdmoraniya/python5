# 2) Write a program to create a class for student with RollNo, Name, Age,Gender and methods named AddStudent() and DisplayStudent() 

class Student:

    def AddStudent(self):
        self.RollNo = input("Enter Roll No: ")
        self.Name = input("Enter Name: ")
        self.Age = input("Enter Age: ")
        self.Gender = input("Enter Gender: ")

    def DisplayStudent(self):
        print("Roll No:", self.RollNo)
        print("Name:", self.Name)
        print("Age:", self.Age)
        print("Gender:", self.Gender)


s = Student()

s.AddStudent()
s.DisplayStudent()