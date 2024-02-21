# Desenvolva um programa para calcular e mostrar o desconto no valor de uma compra (fornecido pelo usuário), de acordo com a tabela:

# +---------------------------------------------------------+
# |Menor ou igual que R$ 1000 = 10% desconto                |
# +---------------------------------------------------------+
# |Maior que R$ 1000 e menor ou igual a 5000 = 20% desconto |
# +---------------------------------------------------------+
# |Maior que R$ 5000 = 30% desconto                         |
# +---------------------------------------------------------+

valorCompra = float(input("Digite o valor da compra: "))

if valorCompra <= 1000:
    desconto = valorCompra * 0.1
elif valorCompra > 1000 and valorCompra <= 5000:
    desconto = valorCompra * 0.2
elif valorCompra > 5000:
    desconto = valorCompra * 0.3

print(f'O valor do desconto é de R${desconto:.2f}')