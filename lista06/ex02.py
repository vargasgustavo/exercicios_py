# Escreva uma função que calcula a média dos elementos em uma lista de números.

lista = [10,6,7,4,9,5]

def media(lista):
    soma = 0
    for i in lista:
        soma += i
    media = soma / len(lista) # len(lista) ou 6
    return media

print(media(lista))