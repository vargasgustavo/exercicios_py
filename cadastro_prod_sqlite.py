# CADASTRO DE PRODUTOS EM SQLITE =========================================================================

import sqlite3

# Função para criar a tabela de produtos
def criar_tabela_produtos(conexao):
    cursor = conexao.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS produtos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            quantidade INTEGER,
            preco REAL
        )
    ''')
    conexao.commit()

# Função para cadastrar um novo produto
def cadastrar_produto(conexao, nome, quantidade, preco):
    cursor = conexao.cursor()
    cursor.execute('''
        INSERT INTO produtos (nome, quantidade, preco)
        VALUES (?, ?, ?)
    ''', (nome, quantidade, preco))
    conexao.commit()

# Função para listar todos os produtos cadastrados
def listar_produtos(conexao):
    cursor = conexao.cursor()
    cursor.execute('SELECT * FROM produtos')
    produtos = cursor.fetchall()
    if produtos:
        for produto in produtos:
            print(f"ID: {produto[0]}, Nome: {produto[1]}, Quantidade: {produto[2]}, Preço: R${produto[3]}")
    else:
        print("Não há produtos cadastrados.")

# Função para editar um produto existente
def editar_produto(conexao, id_produto, nome, quantidade, preco):
    cursor = conexao.cursor()
    cursor.execute('''
        UPDATE produtos
        SET nome=?, quantidade=?, preco=?
        WHERE id=?
    ''', (nome, quantidade, preco, id_produto))
    conexao.commit()

# Função para deletar um produto
def deletar_produto(conexao, id_produto):
    cursor = conexao.cursor()
    cursor.execute('''
        DELETE FROM produtos
        WHERE id=?
    ''', (id_produto,))
    conexao.commit()

# Conexão com o banco de dados SQLite
conexao = sqlite3.connect('cadastro_produtos.db')

# Criar tabela de produtos (se não existir)
criar_tabela_produtos(conexao)

# Exemplo de cadastro de produtos
cadastrar_produto(conexao, "Notebook", 5, 3500.00)
cadastrar_produto(conexao, "Smartphone", 10, 2000.00)
cadastrar_produto(conexao, "Fones de ouvido", 20, 300.00)

# Listar todos os produtos cadastrados
print("Produtos cadastrados:")
listar_produtos(conexao)

# Editar um produto existente
editar_produto(conexao, 2, "Smartphone Plus", 15, 2200.00)

# Listar todos os produtos após a edição
print("\nProdutos após a edição:")
listar_produtos(conexao)

# Deletar um produto
deletar_produto(conexao, 1)

# Listar todos os produtos após a exclusão
print("\nProdutos após a exclusão:")
listar_produtos(conexao)

# Fechar conexão com o banco de dados
conexao.close()
