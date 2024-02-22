# Faça um algoritmo para ler dois números inteiros e escrever o maior.

n1 = int(input("Digite um valor inteiro: "))
n2 = int(input("Digite um valor inteiro: "))

maior = 0

if n1 > n2:
    maior = n1
elif n1 < n2:
    maior = n2

print(f"O maior número digitado é {maior}")