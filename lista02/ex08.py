# A prefeitura de Contagem abriu uma linha de crédito para os funcionários estatutários.
# O valor máximo da prestação não poderá ultrapassar 30% do salário bruto.
# Fazer um algoritmo que permita entrar com salário bruto e o valor da prestação, e informar se o empréstimo
# pode ou não ser concedido.

salario_bruto = float(input("Digite o salário bruto: "))
valor_prestacao = float(input("Digite o valor da prestação: "))

limite_prestacao = salario_bruto * 0.30

if valor_prestacao <= limite_prestacao:
    print("Empréstimo concedido!")
else:
    print(f'Empréstimo não concedido. Valor da prestação: {valor_prestacao} excede 30% do salário bruto: {salario_bruto}.')