# Faça um programa que receba um número e diga se est número está no intervalo entre 100 e 200.

num = float(input("Digite um valor: "))

if num >= 100 and num <= 200:
    print("O valor é entre 100 e 200")
elif num < 100:
    print("O valor é menor que 100")
elif num > 200:
    print("O valor é maior que 200")
