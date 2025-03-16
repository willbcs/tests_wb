import os

def verificaHora(mensagem):
    while True:
        h = input(mensagem)
        if h.isdigit() and int(h):
            if int(h) <= 23 and int(h) >= 0:
                os.system('cls')
                return int(h)
            else:
                os.system('cls')
                print('Esse não é um valor aceitável para horas!')
        else:
            os.system('cls')
            print('Por favor, digite apenas números inteiro entre 0 e 24!')

def verificaMinuto(mensagem):
    while True:
        m = input(mensagem)
        if m.isdigit() and int(m):
            if int(m) <= 59 and int(m) >= 0:
                os.system('cls')
                return int(m)
            else:
                os.system('cls')
                print('Esse não é um valor aceitável para minutos!')
        else:
            os.system('cls')
            print('Por favor, digite apenas números')

def mostrarHora():
    h = verificaHora('Digite o horário: ')
    m = verificaMinuto('Digite os minutos: ')
    if h >= 0 and h <= 11:
        os.system('cls')
        print(f'Bom dia! Agora são {h} horas e {m} minutos!')
    elif h >= 12 and h <= 17:
        os.system('cls')
        print(f'Boa tarde! Agora são {h} horas e {m} minutos!')
    elif h >= 18 and h <= 23:
        os.system('cls')
        print(f'Boa noite! Agora são {h} horas e {m} minutos!')

if __name__ == '__main__':
    mostrarHora()