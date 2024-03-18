# Crie uma classe chamada Pessoa com atributos para nome, idade e gênero.
# Adicione métodos para atualizar esses atributos.

class Pessoa:
    def __init__(self, nome, idade, genero):
        self.nome = nome
        self.idade = idade
        self.genero = genero
    
    def atualiza(self, new_nome, new_idade):
        self.nome = new_nome
        self.idade = new_idade
        
    def imprime(self):
        print(f"Nome: {self.nome}, Idade: {self.idade}, Genero: {self.genero}")
    
pessoa1 = Pessoa("José", 50, "m")

pessoa1.imprime()

pessoa1.atualiza("Claudio", 60)

pessoa1.imprime()
