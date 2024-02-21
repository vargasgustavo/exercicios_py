# Escreva um programa para ler três notas obtidas por um aluno durante o semestre. 
#Calcular a sua média (aritmética) e informar a sua mensão Aprovado (média >= 7), Reprovado (média <= 5) e Recuperação (média >= 5.1 and media <= 6.9).

n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
n3 = float(input("Digite a terceira nota: "))

media = (n1 + n2 + n3) / 3

if media >= 7:
    print(f'Aprovado com media {media}')
elif media < 7:
    print(f'Reprovado com media {media}')
