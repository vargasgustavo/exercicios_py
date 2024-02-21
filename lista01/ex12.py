# Faça um programa para ler três números e informar se eles podem ou não ser lados de um triângulo.
# Caso os lados formem um triângulo, indique se o mesmo é: equilátero, isóceles ou escaleno.
# Observação: Um triângulo é equilátero quando possui os três lados iguais, isóceles quando posuui dois lados iguais e escaleno quando não pussui nenhum dos lados iguais.

n1 = float(input("Digite um valor: "))
n2 = float(input("Digite um valor: "))
n3 = float(input("Digite um valor: "))

if n1 == n2 == n3:
    print("É um triângulo equilátero")
elif n1 != n2 or n1 != n3 or n2 != n3:
    print("É um triângulo isósceles")
elif n1 != n2 and n1 != n3:
    print("É um triângulo escaleno")