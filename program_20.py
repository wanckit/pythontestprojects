class Car:
    def __init__(self):
        self.speed = 10
    def calcVelocity(self,x):
        return 3*x*10

examplecar = Car()
print examplecar.calcVelocity(20)
print examplecar.speed
