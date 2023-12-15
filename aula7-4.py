class Triangulo:

    def __init__(self, base, altura, lado_a, lado_b, lado_c, angulo_ab, angulo_ac, angulo_bc):
        self.__base = base
        self.__altura = altura
        self.__lado_a = lado_a
        self.__lado_b = lado_b
        self.__lado_c = lado_c
        self.__angulo_ab = angulo_ab
        self.__angulo_ac = angulo_ac
        self.__angulo_bc = angulo_bc

    @property
    def base(self):
        return self.__base
    @property
    def altura(self):
        return self.__altura
    @property
    def lado_a(self):
        return self.__lado_a
    @property
    def lado_b(self):
        return self.__lado_b
    @property
    def lado_c(self):
        return self.__lado_c
    @property
    def angulo_ab(self):
        return self.__angulo_ab
    @property
    def angulo_ac(self):
        return self.__angulo_ac
    @property
    def angulo_bc(self):
        return self.__angulo_bc
    @property
    def area(self):
        return (self.__base * self.__altura) / 2
    @property
    def perimetro(self):
        return self.__lado_a + self.__lado_b + self.__lado_c
    @property
    def tipo_triangulo(self):
        if self.__lado_a == self.__lado_b and self.__lado_b == self.__lado_c:
            return 'Triângulo Equilátero'
        
        elif self.__lado_a == self.__lado_b or self.__lado_b == self.__lado_c:
            return 'Triângulo Isósceles'
        
        else:
            return 'Triângulo Escaleno'
        
t = Triangulo(3, 3, 3, 2, 5, 90, 30, 60)
print(t.area)
print(t.perimetro)
print(t.tipo_triangulo)