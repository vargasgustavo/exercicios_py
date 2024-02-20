# Crie uma lista com os valores pares e outra com os impares de 1 a 10.

lista_pares = []
lista_impares = []

for i in range(1, 11):
    if i % 2 == 0:
        lista_pares.append(i)
    elif i % 2 == 1:
        lista_impares.append(i)

print(lista_pares)
print(lista_impares)