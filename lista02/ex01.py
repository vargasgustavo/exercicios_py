# Construir um algoritimo que leia dois números e efetue a adição.
# Caso o valor somado seja maior que 20, este deverá ser apresentado somando-se a ele mais 8;
# Caso o valor somado seja menor ou igual a 20, este deverá ser apresentado subritaindo-se 5.

n1 = int(input("Digite um valor: "))
n2 = int(input("Digite um valor: "))

soma = n1 + n2

if soma > 20:
    valor = soma + 8
elif soma <= 20:
    valor = soma - 5

print(valor)