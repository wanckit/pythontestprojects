class Vehicule:
    wheels = 4
    def __int__(self):
        print "Hello"
    def calcVelocity(self,x):
        return 3*x*10        

class Car(Vehicule):
    def __init__(self):
        self.speed = 10

examplecar = Car()
print examplecar.speed
print examplecar.wheels
print examplecar.calcVelocity(20)
        
