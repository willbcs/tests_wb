import os
class Med_Mai:
    def __init__(self):
        self.soma = 0
        self.maior = -2**31
        self.menor = 2**31 - 1
        self.numero = []
        self.media = 0
        self.cont = 0
        self.soma = 0

    def eh_numero(self, mensagem):
        while True:
            num1 = input(mensagem)
            try:
                num_1 = int(num1)
                if num_1 > 0:
                    return num_1
                else:
                    os.system('cls')
                    print('Digite valores maiores que zero!')
            except ValueError:
                os.system('cls')
                print('Caracteres inválidos foram digitados')
    
    def numeros(self):
        soma = 0; maior = -2**31; menor = 2**31 - 1
        numero = []
        for i in range(0, 20):
            num = self.eh_numero("Digite um número inteiro e positivo:\n")
            numero.append(num)
            soma += numero[i]

            if numero[i] > maior:
                maior = numero[i]
            
            elif numero[i] < menor:
                menor = numero[i]
        return (soma, maior, menor, numero)

    def med_mai(self):
        soma, maior, menor, numero = self.numeros()
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
    Med_Mai().med_mai()