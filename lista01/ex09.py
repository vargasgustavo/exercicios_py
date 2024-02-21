# Elabore um programa, que solicite ao usuário a velocidade do veículo e apresente na tela a penalidade, de acordo com a tabela a seguir.

velocidade = float(input("Digite a velocidade: "))

if velocidade <= 60:
    print("Sem penalidade!")
elif velocidade > 60 and velocidade <= 80:
    print("Multa Leve!")
elif velocidade > 80 and velocidade <= 100:
    print("Multa Grave!")
elif velocidade > 100 and velocidade <= 120:
    print("Multa Gravíssima!")
elif velocidade > 120:
    print("Detenção do Condutor!")