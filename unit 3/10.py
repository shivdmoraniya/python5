# 10) Write a program to overload addition (+) and subtraction (-) (Use appropriate methods to overload the same. 

class Number:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return Number(self.value + other.value)

    
    def __sub__(self, other):
        return Number(self.value - other.value)

    def display(self):
        print("Value:", self.value)


n1 = Number(20)
n2 = Number(10)

add = n1 + n2
sub = n1 - n2

print("Addition Result:")
add.display()

print("Subtraction Result:")
sub.display()