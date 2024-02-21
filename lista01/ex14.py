# Faça um programa que leia três números e mostre o maior eo menor deles.

n1 = float(input("Digite um valor: "))
n2 = float(input("Digite um valor: "))
n3 = float(input("Digite um valor: "))

maior = 0
menor = 0

if n1 > n2 and n1 > n3:
    maior = n1
elif n1 < n2 and n1 < n3:
    menor = n2

if n2 > n1 and n2 > n3:
    maior = n2
elif n2 < n1 and n2 < n3:
    menor = n2

if n3 > n1 and n3 > n2:
    maior = n3
elif n3 < n1 and n3 < n2:
    menor = n3

print(f'Dentre os números digitados o maior é o número {maior} e o menor é o número {menor}.')