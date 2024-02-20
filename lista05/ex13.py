# Dada uma lista de palavras, crie uma nova lista apenas com as palavras que começam com a letra 'A'.

palavras = ['Abacate', 'Banana', 'Abacaxi', 'Damasco', 'Pera', 'Figo', 'Goiaba', 'Laranja', 'Maça', 'Melancia', 'Romã', 'Côco','Manga', 'Mirtilo', 'Franboesa', 'Morango']

nova_lista = []

for i in palavras:
    if i[0] == 'A':
        nova_lista.append(i)

print(nova_lista)