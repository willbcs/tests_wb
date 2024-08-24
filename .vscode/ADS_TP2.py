import os
c = True
while c == True:
    fatorial = 1
    sNumero = input("Digite o número que deseja calcular o fatorial.\n")
    
    while not sNumero.isdigit() or int(sNumero) < 0:
        sNumero = input("\nInválido! Digite o número que deseja calcular o fatorial.\n")

    numero = int(sNumero)
        
    if numero != 1 and numero != 0:
        for i in range(numero, 1, -1):
            fatorial *= i
            os.system('cls')
        print(f'O resultado de {numero}! é igual a {fatorial}.')

    else:
        print(f'O valor de {numero}! é 1.\n')

    sair = input('\nAperte [S]air ou [C]ontinuar!\n').lower()
    
    while not sair.isalpha() or (sair != "s" and sair != "c"):
        sair = input('\nInválido! Aperte [S]air ou [C]ontinuar!\n').lower()
    
    if sair == "s":
        c = False
    os.system('cls')



