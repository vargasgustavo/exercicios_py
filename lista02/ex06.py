# Faça um algoritmo para ler dois números inteiros A e B e informar se A é divisível por B.

n1 = int(input("Digite um valor inteiro: "))
n2 = int(input("Digite um valor inteiro: "))

if n2 == 0:
    print(f"Não é possível realizar a divisão por {n2}")
elif n1 % n2 == 0:
    print(f"{n1} é divisível por {n2}")
else:
    print(f"{n1} não é divisível por {n2}")