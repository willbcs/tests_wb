import os
def peso(x):
    while True:
        p = input(x)
        try:
            p_float = float(p)
            if p_float > 0:
                return float(p)
            else:
                print("Não existem pessoas com peso menor ou igual a 0! ")
        except ValueError:
            print("Caracteres inválidos foram digitados!\n")

def altura(h):
    while True:
        a = input(h)
        try:
            a_float = float(a)
            if a_float != 0:
                return float(a)
            else:
                print("Não existe altura = 0")
        except ValueError:
            print("\nCaracteres inválidos foram digitados!\n")

def calculadora():
    massa = peso("Digite seu peso:\n")
    medida = altura("Digite sua altura:\n")
    
    return (massa / (medida * medida))

def IMC():
    n = calculadora()
    print(f'Seu IMC é {n:.2f}')
    if n < 18.5:
        print("Você está abaixo do peso!")
    elif n >= 18.5 and n <= 24.9:
        print("Você está dentro da faixa de peso!")
    elif n > 24.9 and n < 30:
        print("Você está obeso em grau I!")
    elif n >= 30 and n < 40:
        print("Você está obeso grau II (severa)!")
    else:
        print("Você está obeso grau III (mórbido)!")

if __name__ == '__main__': 
    while True:
        IMC()
        sair = input("\nDigite 's' para sair ou qualquer tecla para continuar: \n").lower()
        if sair == 's':
            os.system('cls')
            print("\nAté logo!")
            break 
        else:
            os.system('cls')