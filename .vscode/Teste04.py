nome = input("Digite um Nome: ")
if all(n.isalpha() for n in nome.split(' ')):
    indice = 0
    while indice < len(nome):
        print(nome[indice])
        indice += 1
else:
    print('Isso não é um nome!')
 