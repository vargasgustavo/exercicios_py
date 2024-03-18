


class Estudante:
    def __init__(self, nome, idade, nota, serie):
        self.nome = nome
        self.idade = idade
        self.nota = nota
        self.serie = serie
        
    def atualiza(self, new_nome, new_idade, new_nota, new_serie):
        self.nome = new_nome
        self.idade = new_idade
        self.nota = new_nota
        self.serie = new_serie
    
    def imprime(self):
        print(f"Nome: {self.nome}, Idade: {self.idade}, Nota: {self.nota}, Série: {self.serie}")
        
estudante1 = Estudante("Caio", 40, 8, 3)

estudante1.imprime()

estudante1.atualiza("Kleber", 30, 7, 5)

estudante1.imprime()