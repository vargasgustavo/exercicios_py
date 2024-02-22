# Em uma empresa paga-se R$ 19.50 a hora e recolhe-se para o imposto de renda 10% dos salários acima de R$ 1500.
# Dado um número de horas trabalhadas por um funcionário, informar o valor do seu salário líquido.

hora = 19.50

horasTrabalhadas = float(input("Digite a quantidade de horas: "))

salarioBruto = hora * horasTrabalhadas

if salarioBruto > 1500:
    salarioLiquido = salarioBruto * 0.9
    print(f"O salário líquido é de R${salarioLiquido:.2f}")
else:
    print(f'O imposto de renda não afetou seu salário.')