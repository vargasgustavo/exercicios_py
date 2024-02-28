# Agenda Telefônica: Implemente uma agenda telefônica utilizando dicionários, 
# onde o usuário pode adicionar contatos, buscar por número de telefone e remover contatos.

agenda_telefonica = {}

while True:
    print("\n=== Agenda Telefônica ===")
    print("1. Adicionar contato")
    print("2. Buscar número de telefone")
    print("3. Remover contato")
    print("4. Listar todos os contatos")
    print("5. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Digite o nome do contato: ")
        telefone = input("Digite o número de telefone: ")
        agenda_telefonica[nome] = telefone
        print(f"Contato {nome} adicionado com sucesso.")
    elif opcao == "2":
        nome = input("Digite o nome do contato para buscar o número de telefone: ")
        if nome in agenda_telefonica:
            print(f"O número de telefone de {nome} é: {agenda_telefonica[nome]}")
        else:
            print("Contato não encontrado na agenda.")
    elif opcao == "3":
        nome = input("Digite o nome do contato que deseja remover: ")
        if nome in agenda_telefonica:
            del agenda_telefonica[nome]
            print(f"Contato {nome} removido com sucesso.")
        else:
            print("Contato não encontrado na agenda.")
    elif opcao == "4":
        print("=== Lista de Contatos ===")
        for nome, telefone in agenda_telefonica.items():
            print(f"Nome: {nome}, Telefone: {telefone}")
    elif opcao == "5":
        print("Saindo da agenda telefônica...")
        break
    else:
        print("Opção inválida. Tente novamente.")
