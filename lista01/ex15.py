# Faça um programa para calcular o peso ideal, a partir da fórmula IMC = peso / altura 2.
# Nesse caso, solicite o peso e a altura do usuário, faça o cálculo e apresente a faixa de risco correspondente, de acordo com a tabela abaixo:

# +---------------------------------------+------------------------------+
# |                Pontos                 |           Conceito           |
# +---------------------------------------+------------------------------+
# | Menor ou igual a 50                   |        Abaixo do peso        |
# +---------------------------------------+------------------------------+
# | Maior que 50 e menor ou igual a 70    |            Normal            |
# +---------------------------------------+------------------------------+
# | Maior que 70 e menor ou igual a 90    |       Excesso de peso        |
# +---------------------------------------+------------------------------+
# | Maior que 90 e menor ou igual a 100   |          Obesidade           |
# +---------------------------------------+------------------------------+
# | Maior que 90 e menor ou igual a 100   |       Obesidade mórbida      |
# +---------------------------------------+------------------------------+

a = float(input("Digite sua altura: "))
s = input("Digite seu sexo ( m / f ): ")

if s == 'm':
    peso_ideal = (72.7 * a) - 58
elif s == 'f':
    peso_ideal = (62.7 * a) - 44.7

if peso_ideal <= 20:
    print(f'Você está abaixo do peso!')
elif peso_ideal > 20 and peso_ideal <= 25:
    print(f'Seu peso está normal!')
elif peso_ideal > 25 and peso_ideal <= 30:
    print(f'Você está com sobrepeso!')
elif peso_ideal > 30 and peso_ideal <= 35:
    print(f'Você está com obesidade!')
elif peso_ideal > 35 and peso_ideal <= 40:
    print(f'Você está com obesidade mórbida!')

print(f'O seu peso ideal é {peso_ideal}')