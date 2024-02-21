# Um posto de combustível vende três tipos de combustível: álcool, disel e gasolina. O preço de cada litro de combustível é apresentado na tabela dea seguir.
# Faça um programa que leia um caractere que representa o tipo de combustível comprado ( a, d ou g ) e a quantidade em litros.
# O programa deve imprimir o valor em reais a ser pago pelo combustível.

alcool = 1.7997
disel = 0.9789
gasolina = 2.1009

motorista = input("Digite o tipo de combustível ( a / d / g ): ")

litros = float(input("Digite a quantidade de litro para abastecer: "))

if motorista == 'a':
    valor = litros * alcool
elif motorista == 'd':
    valor = litros * disel
elif motorista == 'g':
    valor = litros * gasolina

print(f'O valor a ser pago é de R${valor:.2f}')