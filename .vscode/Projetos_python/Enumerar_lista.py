lista = ['Maria', 'João', 'Antônio', 'Lúcio', True, 10]
lista.append('Carlos')
lista.append('Ernesto')
lista2 = ['Mario', 'Sílvia', 122]
lista.extend(lista2)

for nome in lista:
    print([lista.index(nome)], nome)

_, nome2, *resto = lista2
print(nome2, resto, 'ESSE')

lista_enumerada = enumerate(lista)
for nome in lista_enumerada:
    print(nome, 'ESSE 2')
 #ou
    
for item in enumerate(lista):
    print(item, 'ESSE 3')

lista_enumerada = list(enumerate(lista))
print(lista_enumerada)
 
for indice, nome3 in enumerate(lista):
    print(indice, nome3)