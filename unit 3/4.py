# 4) Write a program to make use of inner class 

class Student:

    def __init__(self, name, roll):
        self.name = name
        self.roll = roll
        self.lap = self.Laptop()   

    def show(self):
        print("Name:", self.name)
        print("Roll No:", self.roll)
        self.lap.display()

    class Laptop:
        def __init__(self):
            self.brand = "Dell"
            self.ram = "8GB"

        def display(self):
            print("Laptop Brand:", self.brand)
            print("RAM:", self.ram)


s1 = Student("Natho", 101)

s1.show()