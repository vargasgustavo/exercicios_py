# Imagine uma prova com 100 questões, em cada uma delas vale 1 ponto. 
# Nesse caso, faça um programa para divulgar o resultado a partir de conceitos, de acordo com a seguinte tabela:

# +---------------------------------------+------------------------------+
# |                Pontos                 |           Conceito           |
# +---------------------------------------+------------------------------+
# | Menor ou igual a 50                   |               D              |
# +---------------------------------------+------------------------------+
# | Maior que 50 e menor ou igual a 70    |               C              |
# +---------------------------------------+------------------------------+
# | Maior que 70 e menor ou igual a 90    |               B              |
# +---------------------------------------+------------------------------+
# | Maior que 90 e menor ou igual a 100   |               A              |
# +---------------------------------------+------------------------------+

pontos = int(input("Digite o número de pontos: "))

if pontos <= 50:
    conceito = "D"
elif pontos > 50 and pontos <= 70:
    conceito = "C"
elif pontos > 70 and pontos <= 90:
    conceito = "B"
elif pontos > 90 and pontos <= 100:
    conceito = "A"

print(f'O conceito é {conceito}')