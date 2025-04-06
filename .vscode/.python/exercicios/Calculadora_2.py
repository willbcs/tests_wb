class Calculadora:

    def soma (self, a,b):
        return (a + b)

    def subtração (self, a,b):
        return (a - b)

    def divisão (self, a,b):
        return (a / b)

    def multiplicação (self, a,b):
        return (a * b)

    def quadrado (self, x):
        return x*x

    def eh_numero (self, texto):
        while True:
            numero = input(texto)
            try:
                return float(numero)
            except ValueError:
                print("Caracteres inválidos foram digitados: ")

    def calcular(self):
        while True:
            print("=+"*20)
            print("              CALCULADORA")
            print("=+"*20)
            print("1. SOMA")
            print("2. SUBTRAÇÃO")
            print("3. MULTIPLICAÇÃO")
            print("4. DIVISÃO")
            print("5. ELEVAR AO QUADRADO")
            print("6. SAIR")

            operacao = input("Escolha uma opção: ")

            if operacao == '6':
                print("Até logo!\n")
                break
            
            elif operacao == '5':
                num1 = self.eh_numero("Digite o número a ser elevado ao quadrado: ")
                print(f'O resultado é: {self.quadrado(num1)}\n')

            elif operacao == '4':
                num1 = self.eh_numero("Digite o primeiro número: ")
                while True:
                    num2 = self.eh_numero("Digite o segundo número: ")
                    if num2 == 0:
                        print("Erro! Divisão por zero não é possível.")
                    else:
                        print(f'O resultado da divisão é: {self.divisão(num1,num2)}\n')
                        break

            elif operacao == '3':
                num1 = self.eh_numero("Digite o primeiro número: ")
                num2 = self.eh_numero("Digite o segundo número: ")
                print(f'A resultado da multiplicação é: {self.multiplicação(num1,num2)}')

            elif operacao == '2':
                num1 = self.eh_numero("Digite o primeiro número: ")
                num2 = self.eh_numero("Digite o segundo número: ")
                print(f'A resultado da subtração é: {self.subtração(num1,num2)}')
            
            elif operacao == '1':
                num1 = self.eh_numero("Digite o primeiro número: ")
                num2 = self.eh_numero("Digite o segundo número: ")
                print(f'A resultado da soma é: {self.soma(num1,num2)}')

            else:
                print('\nOpção inválida!\n ')

if __name__ == "__main__":
    calc = Calculadora()
    calc.calcular()