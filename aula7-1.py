# Area do quandrado

class Quadrado:

    def __init__(self, base):
        self.__base = base

    @property
    def area(self):
        return self.__base ** 2
    @property
    def perimetro(self):
        return self.__base * 4

altura = int(input('Digite a altura do quadrado: '))

quadrado = Quadrado(altura)
print(quadrado.area)
print(quadrado.perimetro)
