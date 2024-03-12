# Criando um dicionário para armazenar os produtos
cadastro_produtos = {}

# Função para adicionar um produto ao cadastro
def adicionar_produto(codigo, nome, preco, estoque):
    if codigo not in cadastro_produtos:
        cadastro_produtos[codigo] = {'nome': nome, 'preco': preco, 'estoque': estoque}
        print(f"Produto {nome} adicionado com sucesso!")
    else:
        print("Este código de produto já está em uso.")

# Função para buscar um produto pelo código
def buscar_produto(codigo):
    if codigo in cadastro_produtos:
        produto = cadastro_produtos[codigo]
        print(f"Nome: {produto['nome']}, Preço: R${produto['preco']}, Estoque: {produto['estoque']}")
    else:
        print("Produto não encontrado.")

# Função para atualizar o estoque de um produto
def atualizar_estoque(codigo, novo_estoque):
    if codigo in cadastro_produtos:
        cadastro_produtos[codigo]['estoque'] = novo_estoque
        print("Estoque atualizado com sucesso!")
    else:
        print("Produto não encontrado.")

# Função para exibir todos os produtos cadastrados
def exibir_cadastro():
    print("Cadastro de Produtos:")
    for codigo, produto in cadastro_produtos.items():
        print(f"Código: {codigo}, Nome: {produto['nome']}, Preço: R${produto['preco']}, Estoque: {produto['estoque']}")

# Exemplos de utilização
adicionar_produto(1, "Camisa", 25.99, 100)
adicionar_produto(2, "Calça", 39.99, 50)
adicionar_produto(3, "Boné", 15.50, 75)

exibir_cadastro()

buscar_produto(2)

atualizar_estoque(1, 80)

exibir_cadastro()