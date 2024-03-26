# Crie uma classe chamada Funcionario com atributos para nome, cargo e salário.
# Adicione métodos para calcular o aumento de salário.

class Funcionario():
    def __init__(self, nome, cargo, salario):
        self.nome = nome
        self.cargo = cargo
        self.salario = salario

    def aumenta_salario(self, valor):
        self.salario += valor

    def atualiza_cargo(self, new_cargo):
        self.cargo = new_cargo

    def imprime_salario(self):
        print(f'O salário do {self.nome} é de R${self.salario:.2f}')

funcionario1 = Funcionario("Breno", "Gerente", 4236)

funcionario1.imprime_salario()

funcionario1.aumenta_salario(500)

funcionario1.imprime_salario()