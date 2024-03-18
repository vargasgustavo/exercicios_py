# Crie uma classe chamada Produto com atributos para nome, preço e quantidade em estoque.
# Adicione métodos para atualizar o preço e a quantidade, e para exibir informações sobre o produto.

class Produto:
    def __init__(self, nome, preco, qtde_estoque):
        self.nome = nome
        self.preco = preco
        self.qtde_estoque = qtde_estoque
        
    def atualiza(self, new_preco, new_estoque):
        self.preco = new_preco
        self.qtde_estoque = new_estoque
        
    def imprime(self):
        print(f"Nome: {self.nome}, Preço: R${self.preco}, Estoque: {self.qtde_estoque}")
        
produto1 = Produto("Banana", 5, 10)

produto1.imprime()

produto1.atualiza(10, 20)

produto1.imprime()