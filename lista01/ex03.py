# Escreva um programa que leia dois valores inteiros distintos e informe qual é o maior.

n1 = int(input("Digite um valor: "))
n2 = int(input("Digite um valor: "))

maior = 0

if n1 > n2:
    maior = n1
elif n1 < n2:
    maior = n2

print(f'O maior numero digitado foi {maior}')
