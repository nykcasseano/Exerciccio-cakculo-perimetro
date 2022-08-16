import math

class Circulo():
    
    def __init__(self, r):
        self.r = r
    
    def calcula_area(self):
        return math.pi*self.r**2
    
    def calcula_perimetro(self):
        return 2*math.pi*self.r