#nome = 'Bruno'
#preco = 1000.95897643
#variavel = '%s, o preço é R$%.2f' % (nome, preco)
#print(variavel)
#print(f'{nome}, o preço é R${preco:.2f}')
#print(nome[0:5:2])
#print(nome[-1:-6:-1]) len tamanho
nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')
if nome and idade:
    if all(n.isalpha() for n in nome.split(' ')) and idade.isdigit:
        print('Seu nome é:', nome)
        print('Seu nome invertido é:', nome[::-1])
        print('Seu nome utiliza', len(nome), 'caracteres')
        print("A primeira letra do seu nome é:", nome[0])
        print("A última letra do seu nome é:", nome[-1])
        if ' ' in nome:
            print("O seu nome contem espaços")
        else:
            print('Seu nome não contem espaços')
    else:
       print('Desculpe, você digitou nome ou idade incorretamente!')     
else:
    print('Desculpe, você deixou campos em branco') 
