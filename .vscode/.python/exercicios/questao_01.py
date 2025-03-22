import os

def eh_numero(mensagem):
    while True:
        num = input(mensagem)
        try:
            numero = int(num)
            if numero >= 0:
                return numero
            else:
                os.system('cls')
                print('Digite um valor maior ou igual a zero! ')
        except ValueError:
            os.system('cls')
            print('Caracteres inválidos foram digitados')

def fibonacci():
    numero = eh_numero("Digite um número:\n")
    a = 1
    b = 1
    prox_termo = 1
    while prox_termo < numero:
        soma = a + b
        prox_termo = soma
        a = b 
        b = soma

    if numero == 0 or numero == 1:
        print("O valor digitado pertence à sequência de Fibonacci.")

    elif prox_termo == numero:
        print("O Valor digitado pertence a sequência de Fibonacci.")

    elif prox_termo != numero:
        return print("O Valor digitado NÃO pertence a sequência de Fibonacci.")

fibonacci()