#Crie uma função que converte uma temperatura de Celsius para Fahrenheit (use a fórmula: F = C * 9/5 + 32).

def celsius_to_fahrenheit(celsius):
    fahrenheit = celsius * 9/5 + 32
    return fahrenheit

celsius = float(input('Digite a temperatura em Celsius: '))

fahrenheit = celsius_to_fahrenheit(celsius)

print(f'A temperatura em Fahrenheit é de {fahrenheit:.2f}°F')
