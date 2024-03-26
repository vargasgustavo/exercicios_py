# Crie uma classe chamada Calendario que tenha métodos para receber a data atual, verificar se é um ano bissexto e exibir o dia da semana.

import datetime

class Calendario:
    def __init__(self):
        pass
    
    def obter_data_atual(self):
        return datetime.datetime.now()
    
    def é_ano_bissexto(self, ano):
        if ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0):
            return True
        else:
            return False
    
    def dia_da_semana(self, data):
        dias_da_semana = ['Segunda-feira', 'Terça-feira', 'Quarta-feira', 'Quinta-feira', 'Sexta-feira', 'Sábado', 'Domingo']
        return dias_da_semana[data.weekday()]

# Exemplo de uso
calendario = Calendario()

# Obter data atual
data_atual = calendario.obter_data_atual()
print("Data atual:", data_atual)

# Verificar se é um ano bissexto
ano = data_atual.year
if calendario.é_ano_bissexto(ano):
    print(ano, "é um ano bissexto.")
else:
    print(ano, "não é um ano bissexto.")

# Exibir o dia da semana
print("Dia da semana:", calendario.dia_da_semana(data_atual))
