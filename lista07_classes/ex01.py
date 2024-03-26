# Crie uma classe chamada Retangulo que tenha métodos para calcular a área e o perímetro do retângulo, dados os valores dos lados.

class Retangulo:
    def __init__(self, lado1, lado2):
        self.lado1 = lado1
        self.lado2 = lado2

    def area(self):
        return self.lado1 * self.lado2
    
    def perimetro(self):
        return (self.lado1 * 2) + (self.lado2 * 2)
    
    def imprime_area(self):
        print(f'A área do retângulo é {self.area()}')
    
    def imprime_perimetro(self):
        print(f'O perímetro do retângulo é {self.perimetro()}')
        
retangulo1 = Retangulo(5, 8)
retangulo1.imprime_area()

retangulo1.imprime_perimetro()