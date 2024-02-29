# Faça um programa para calcular o peso ideal, a partir da fórmula IMC = peso / altura 2.
# Nesse caso, solicite o peso e a altura do usuário, faça o cálculo e apresente a faixa de risco correspondente, de acordo com a tabela abaixo:

# +---------------------------------------+------------------------------+
# |                Pontos                 |           Conceito           |
# +---------------------------------------+------------------------------+
# | Menor ou igual a 20                   |        Abaixo do peso        |
# +---------------------------------------+------------------------------+
# | Maior que 20 e menor ou igual a 25    |            Normal            |
# +---------------------------------------+------------------------------+
# | Maior que 25 e menor ou igual a 30    |       Excesso de peso        |
# +---------------------------------------+------------------------------+
# | Maior que 30 e menor ou igual a 35    |          Obesidade           |
# +---------------------------------------+------------------------------+
# | Maior que 25 e menor ou igual a 40    |       Obesidade mórbida      |
# +---------------------------------------+------------------------------+

a = float(input("Digite sua altura: "))
p = float(input("Digite seu peso: "))

imc = p / (a ** 2)

if imc <= 20:
    print(f'Você está abaixo do peso!')
elif imc > 20 and imc <= 25:
    print(f'Seu peso está normal!')
elif imc > 25 and imc <= 30:
    print(f'Você está com sobrepeso!')
elif imc > 30 and imc <= 35:
    print(f'Você está com obesidade!')
elif imc > 35 and imc <= 40:
    print(f'Você está com obesidade mórbida!')