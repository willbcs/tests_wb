import os
def Valor(mensagem):
    while True:
        v = input(mensagem)
        try:    
            v_float = float(v)
            if v_float > 0:
                return v_float
            else:
                os.system('cls')
                print("O valor digitado precisa ser maior que zero!\n ")                
        except ValueError:
            os.system('cls')
            print("Caracteres inválidos foram digitados!\n ")

def Menu():
    while True:
        print("\nESCOLHA A OPÇÃO DE PAGAMENTO DESEJADA:")
        print("1 - DINHEIRO")
        print("2 - À VISTA NO CARTÃO")
        print("3 - PARCELADO NO CARTÃO EM 2X")
        print("4 - PARCELADO NO CARTÃO EM 3X OU MAIS")
        print("5 - SAIR")
        pagamento = input("\nEscolha uma opção:\n")
        try:
            o_pagamento = int(pagamento)
            if o_pagamento in (1, 2, 3, 4, 5):
                return o_pagamento
            else:
                print("Opção inválida! ")  
        except ValueError:
            print("\nCaracteres inválidos foram digitados!\n")
            
def Pagamento():
    while True:
        preco = Valor("Digite o valor do produto:\n")
        opcao = Menu()
        os.system('cls')
        
        if opcao == 1:
            total_1 = preco - (preco * 0.15)
            print(f"\nÀ vista e em dinheiro, o valor total é de R${total_1:.2f} ")
           
        elif opcao == 2:
            total_2 = preco - (preco *0.1) 
            print(f"\nÀ vista no cartão, o valor total é de R${total_2:.2f} ")
            
        elif opcao == 3:
            print(f"\nParcelado em 2x, o valor total é de R${preco:.2f} ")
          
        elif opcao == 4:
            total_3 = preco + (preco * 0.1)
            print(f"\nParcelado em 3x ou mais, o valor total é de R${total_3:.2f} ")
            
        else:                   
            break            

        print("\nDeseja realizar uma nova operação?")
        fim = input("Digite 's' para sair ou qualquer tecla para continuar:\n").lower()
        if fim == 's':
            os.system('cls')
            print("Até Logo!!")
            break
        else:
            os.system('cls')

if __name__== "__main__":
    Pagamento()