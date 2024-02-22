# Faça um algoritmo para ler um número inteiro e informar se o número é par ou ímpar.

num = int(input("Digite um valor inteiro: "))

if num % 2 == 0:
    print(f"O número {num} é par")
elif num % 2 == 1:
    print(f"O número {num} é ímpar")