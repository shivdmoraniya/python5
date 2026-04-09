# 9) Write a program to create interface and utilize the same in other class. 

from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):
    def sound(self):
        print("Dog barks")


d = Dog()
d.sound()