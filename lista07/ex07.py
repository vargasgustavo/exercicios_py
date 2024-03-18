# Crie uma classe chamada Animal com métodos para fazer o animal emitir som e 
# para exibir informações básicas sobre o animal (por exemplo, espécie, cor).

class Animal:
    def __init__(self, especie, cor):
        self.especie = especie
        self.cor = cor
    
    def emitir_som(self):
        pass
    
    def exibir_informacoes(self):
        print("Espécie:", self.especie)
        print("Cor:", self.cor)

# Exemplo de uso
class Cachorro(Animal):
    def __init__(self, cor):
        super().__init__("Cachorro", cor)
    
    def emitir_som(self):
        print("Au au!")

class Gato(Animal):
    def __init__(self, cor):
        super().__init__("Gato", cor)
    
    def emitir_som(self):
        print("Miau!")

# Teste das classes
cachorro = Cachorro("Marrom")
cachorro.exibir_informacoes()
cachorro.emitir_som()

print()

gato = Gato("Branco")
gato.exibir_informacoes()
gato.emitir_som()
