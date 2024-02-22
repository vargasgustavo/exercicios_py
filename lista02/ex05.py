# Escreva um algoritmo que receba um número e imprima uma das mensagens: "é múltiplo de 3" ou "não é múltiplo de 3".

num = int(input("Digite um valor inteiro: "))

if num % 3 == 0:
    print(f'O número {num} é divisível por 3')
else:
    print(f'O número {num} não é divisível por 3')