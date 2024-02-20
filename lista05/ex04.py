# Dada uma lista de palavras, crie uma nova lista com o comprimento de cada palavra.

palavras = ['Python', 'C++', 'Java', 'PHP', 'JavaScript', 'Kotlin']

lista = []

for i in palavras:
    lista.append(len(i))

print(lista)