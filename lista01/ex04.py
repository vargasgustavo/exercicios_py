# Desenvolva um programa que solicite dois números inteiros, mostre a soma destes números, e avise se a soma é maior, menor ou igual a 1000.

n1 = int(input("Digite um valor: "))
n2 = int(input("Digite um valor: "))

soma = n1 + n2

if soma > 1000:
    print("A soma é maior que 1000")
elif soma < 1000:
    print("A soma é menor que 1000")
elif soma == 1000:
    print("A soma é igual a 1000")
