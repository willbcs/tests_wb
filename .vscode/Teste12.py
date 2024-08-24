import os
def eh_numero(mensagem):
    while True:
        num1 = input(mensagem)
        try:
            num_1 = int(num1)
            if num_1 > 0:
                return num_1
            else:
                os.system('cls')
                print('Digite valores maiores que zero! ')
        except ValueError:
            os.system('cls')
            print('Caracteres inválidos foram digitados')

def Numeros():
    soma = 0; maior = -2**31; menor = 2**31 - 1
    numero = []
    for i in range(0, 20):
        num = eh_numero("Digite um número inteiro e positivo:\n")
        numero.append(num)
        soma += numero[i]

        if numero[i] > maior:
            maior = numero[i]
        
        if numero[i] < menor:
            menor = numero[i]
    return (soma, maior, menor, numero)

def Med_Mai():
    soma, maior, menor, numero = Numeros()
    media = (soma / len(numero)); cont = 0

    for i in range(len(numero)):
        if numero[i] > media:
            cont += 1

    os.system('cls')
    print(f'A soma dos 20 números é {soma}')
    print(f'O maior número digitado é {maior}')
    print(f'O menor número digitado é {menor}')
    print(f'A média dos números digitados é {media:.2f}')
    print(f'A quantidade de números maior que a média é {cont}')

if __name__=="__main__":
    Med_Mai()