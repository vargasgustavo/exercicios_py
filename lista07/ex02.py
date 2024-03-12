# Crie uma classe chamada ContaBancaria que tenha métodos para depositar, sacar e verificar saldo.

class ContaBancaria:
    def __init__(self, agencia, conta, saldo):
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo
    
    def depositar(self, valor):
        self.saldo += valor
        return self.saldo
    
    def sacar(self, valor):
        self.saldo -= valor
        return self.saldo
    
    def verificar_saldo(self):
        return self.saldo

