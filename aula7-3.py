from math import pi

class Circulo:

    def __init__(self, raio):
        self.raio = raio

    @property
    def diametro(self):
        return self.raio * 2 
    
    @property
    def area(self):
        return (pi * self.raio) ** 2
    
    @property
    def perimetro(self):
        return (2 * pi) * self.raio

raio = float(input('Digite o raio do circulo: '))

c = Circulo(raio)
print(c.diametro)
print(f'{c.area:.3f}')
print(f'{c.perimetro:.3f}')