# Implemente uma função que conta o número de vogais em uma palavra.

def conta_vogais(palavra):
    vogais = 0
    for letra in palavra:
        if letra in "aeiou":
            vogais += 1
    return vogais

print(conta_vogais("abracadabra"))