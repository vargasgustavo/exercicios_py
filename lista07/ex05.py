# Crie uma classe chamada Triangulo com métodos para calcular a área e o perímetro do triângulo, 
# dados os valores dos lados.

class Triangulo:
    def __init__(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3
    
    def area(self):
        return (self.lado1 * self.lado2) / 2
    
    def perimetro(self):
        return self.lado1 + self.lado2 + self.lado3
    
    def imprime(self):
        print(f'A área do triângulo é {self.area()}')
        print(f'O perímetro do triângulo é {self.perimetro()}')

triangulo1 = Triangulo(8, 9, 4)

triangulo1.area()

triangulo1.perimetro()

triangulo1.imprime()