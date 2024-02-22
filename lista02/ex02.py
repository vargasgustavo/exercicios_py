# Escreva um algoritmo em que leia um número e imprima 
# a raiz quadrada do número caso ele seja positivo ou igual a zero e o quadrado do número caso ele seja negativo.
# Obs: Usar a biblioteca math.h

import math

num = int(input("Digite um valor: "))

if num >= 0:
    calc = math.sqrt(num)
elif num < 0:
    calc = (num * num)

print(calc)