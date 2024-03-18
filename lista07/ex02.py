# Crie uma classe chamada ContaBancaria que tenha métodos para depositar, sacar e verificar saldo.

class ContaBancaria:
    def __init__(self, saldo):
        self.saldo = saldo
    
    def depositar(self, valor):
        self.saldo += valor
        return self.saldo
    
    def sacar(self, valor):
        self.saldo -= valor
        return self.saldo
    
    def verificar_saldo(self):
        return self.saldo

conta1 = ContaBancaria(5930)

conta1.depositar(2540)

conta1.verificar_saldo()

conta1.sacar(5400)

conta1.verificar_saldo()
