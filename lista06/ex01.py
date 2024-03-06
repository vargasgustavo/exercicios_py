# Crie uma função que recebe uma lista de números e retorna a soma dos números pares contidos na lista.

lista = [1,5,4,8,9,5,7,6]
def somaPar(lista):
    soma = 0
    for i in lista:
        if i % 2 == 0:
            soma += i
    return soma

print(somaPar(lista))