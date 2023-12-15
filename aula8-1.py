class Forma_geometrica():

    def __init__(self, lado):
        self.__lado = lado
    @property
    def lado(self):
        return self.__lado
    
    # @property
    # def area(self):
    #     pass
    # @property
    # def perimetro(self):
        pass

class Quadrado(Forma_geometrica):

    def __init__(self, lado):
        super().__init__(lado)

    @property
    def area(self):
        return self.lado ** 2
    @property
    def perimetro(self):
        return self.lado * 4

# altura = int(input('Digite a altura do quadrado: '))

# quadrado = Quadrado(altura)
# print(quadrado.area)
# print(quadrado.perimetro)

class Retangulo(Forma_geometrica):

    def __init__(self, lado, altura):
        super().__init__(lado)
        self.__altura = altura
       
    @property
    def area(self):
       return self.lado * self.__altura
    
    @property
    def perimetro(self):
        return (self.lado * 2) + (self.__altura * 2)
    
# lado = float(input('Digite a base: '))
# altura = float(input('Digite a altura: '))

# r = Retangulo(lado, altura)
# print(r.area)
# print(r.perimetro)