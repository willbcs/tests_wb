import os

class Fatorial:
    def verifica_digito(self, mensagem):
        while True:
            numero = input(mensagem)
            if numero.isdigit() and (int(numero) >= 0):            
                return int(numero)
            os.system('cls')
            
            print("Precisa ser um número inteiro maior que zero.\n")

    def encerrar(self, mensagem):
        while True:
            sair = input(mensagem).lower()
            while not sair.isalpha() or (sair != "s" and sair != "c"):
                sair = input('\nInválido! Aperte [S]air ou [C]ontinuar!\n').lower()  
            if sair == "s":
                return False
            break
            
    def calcular(self):
        while True:
            fatorial = 1
            numero = self.verifica_digito("Digite o número que deseja calcular o fatorial:\n") 
            os.system('cls') 
            if numero != 1 and numero != 0:
                for i in range(numero, 1, -1):
                    fatorial *= i
                    os.system('cls')
                print(f'O resultado de {numero}! é igual a {fatorial}.\n')
            else:
                print(f'O valor de {numero}! é 1.\n')
            sair = self.encerrar('Aperte [S]air ou [C]ontinuar!\n')
            os.system('cls')
            if sair == False:
                break

if __name__== "__main__":
    Fatorial().calcular()