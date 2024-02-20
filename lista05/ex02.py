# Crie uma lista vazia e adicione os números pares de 2 a 10 a ela.

lista = []

for i in range(2, 11):
    if i % 2 == 0:
        lista.append(i)

print(lista)