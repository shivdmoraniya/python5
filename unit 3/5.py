# 5) Create a Temperature class. Create 2 methods named convertFarenheit() and convertCelsius().  

class Temperature:

    def convertFarenheit(self, c):
        f = (c * 9/5) + 32
        print("Temperature in Fahrenheit:", f)

    def convertCelsius(self, f):
        c = (f - 32) * 5/9
        print("Temperature in Celsius:", c)


t = Temperature()

t.convertFarenheit(25)
t.convertCelsius(77)