# Crie uma classe chamada Livro com atributos para título, autor e número de páginas.
# Adicione métodos para exibir informações sobre o livro.

class Livro:
    def __init__(self, titulo, autor, numero_pagina):
        self.titulo = titulo
        self.autor = autor
        self.numero_pagina = numero_pagina
        
    def imprime(self):
        print(f'{self.titulo} - {self.autor} - {self.numero_pagina}')
        
livro1 = Livro("Anaconda 5", "Cuca Beludo", 600)

livro1.imprime()
