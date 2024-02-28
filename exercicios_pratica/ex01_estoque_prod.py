# Crie um sistema simples de controle de estoque, onde o usuário pode adicionar produtos, 
#quantidades e verificar o estoque disponível.

estoque = {}

while True:
    print("\n=== Sistema de Controle de Estoque ===")
    print("1. Adicionar produto")
    print("2. Verificar estoque")
    print("3. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        produto = input("Digite o nome do produto: ")
        quantidade = int(input("Digite a quantidade a ser adicionada: "))
        if produto in estoque:
            estoque[produto] += quantidade
        else:
            estoque[produto] = quantidade
        print(f"{quantidade} unidades do produto {produto} foram adicionadas ao estoque.")
    elif opcao == "2":
        produto = input("Digite o nome do produto para verificar o estoque: ")
        if produto in estoque:
            print(f"Estoque disponível para {produto}: {estoque[produto]} unidades.")
        else:
            print("Produto não encontrado no estoque.")
    elif opcao == "3":
        print("Saindo do sistema...")
        break
    else:
        print("Opção inválida. Tente novamente.")
