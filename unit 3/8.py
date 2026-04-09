# 8) Write a program to create abstract class with one method. 

from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        print("Area of Square:", self.side * self.side)


s = Square(4)
s.area()