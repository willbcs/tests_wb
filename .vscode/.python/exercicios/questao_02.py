import os

def eh_palavra(mensagem):
    while True:
        string = input(mensagem)
        if string.isalpha():
            return string
        else:
            os.system('cls')
            print("Caracteres inválidos foram digitados.\nDigite apenas uma palavra (sem espaços).\n")

def analise_string():
    string = eh_palavra("Digite uma palavra:\n").lower()
    letra = "a"
    i=0

    for char in string:
        if char == letra:
            i+=1
    
    os.system('cls')
    print(string)
    print(f'\nA letra "A" aparece {i} vezes.\n')

analise_string()