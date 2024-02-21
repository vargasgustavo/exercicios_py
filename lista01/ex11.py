# Tendo como dados de entrada a altura e o sexo de uma pessoa, faça um programa que calcule seu peso ideal, utilizando as seguintes fórmulas:

# Para homens: (72.7 * h) - 58;

# Para mulheres: (62.7 * h) - 44.7;

a = float(input("Digite sua altura: "))
s = input("Digite seu sexo ( m / f ): ")

if s == 'm':
    peso_ideal = (72.7 * a) - 58
elif s == 'f':
    peso_ideal = (62.7 * a) - 44.7

print(f'O seu peso ideal é {peso_ideal}')