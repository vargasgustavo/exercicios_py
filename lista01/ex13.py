# Faça um programa que determine se um ano é bissexto. 
# Observação: são bissextos todos os anos divisíveis por 4, excluindo os que sejam divisíveis por 100, porém, não os que sejam divisíveis por 400.

ano = int(input("Digite um ano: "))

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano {ano} é bissexto')
else:
    print(f'O ano {ano} não é bissexto')