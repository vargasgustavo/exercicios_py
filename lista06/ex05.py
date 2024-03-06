# Escreva uma função que recebe uma matriz e retorna o maior elemento presente nela.

def maior(matriz):
    maior = matriz[0][0]
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] > maior:
                maior = matriz[i][j]
    return maior

