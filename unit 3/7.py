# 7) Use appropriate functions for each classWrite a program to display MRO using multiple inheritance. Multiple inheritance can be done as per your choice. 

class M:
    def showA(self):
        print("Class M Method")

class N:
    def showB(self):
        print("Class N Method")

class O(M, N):
    def showC(self):
        print("Class Q Method")

obj = O()

obj.showA()
obj.showB()
obj.showC()

print("Method Resolution Order:")
print(O.__mro__)