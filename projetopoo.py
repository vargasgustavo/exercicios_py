#cadastro de serviços
servicos= []
while True:
    print ("===============================")
    print("     Cadastro de serviços     ")
    print("1. Cadastro de serviço para manunteção")
    print("2. Consulta de serviço tecnico")
    print("3. Suporte")
    print("4. Sair")
    print("===============================")
    opcao = int(input("Escolha uma opção: "))
    if opcao == 1:
        nome = input("Digite o seu nome: ")
        telefone = input("Digite o telefone do serviço tecnico: ")
        email = input("Digite o email do serviço tecnico: ")
        descricao = input("Digite a descricao do problema: ")
        peca_def= input("qual a peça com defeito: ")
        servicos=([nome, telefone, email,descricao,peca_def])
        print(f"Serviço {nome,"|",telefone} cadastrado realizado com sucesso.")
        
    elif opcao == 2:
        consulta=input("digite o telefone cadastrado: ")
        if consulta in servicos:
            print(f"A ordem de serviço no numero de ",(consulta)," foi encontrada no sistema.")
        else: 
            print(f"A ordem de serviço no numero de ",(consulta)," não foi encontrada no sistema.")
    elif opcao == 3:
        sup=input("Descreva o problema")
        sup_email=input("digiteo email para entrarmos em contato: ")
        sup_telefone=input("digiteo telefone para entrarmos em contato: ")
        servicos.append([sup,sup_telefone,sup_email])
    elif opcao == 4:
        break
    else:
        print("Opção inválida. Tente novamente.")