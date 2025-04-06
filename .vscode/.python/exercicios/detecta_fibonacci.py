import os

class Fibonacci:
    def eh_numero(self, mensagem):
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

    def calcular(self):
        numero = self.eh_numero("Digite um número:\n")
        if numero == 0 or numero == 1:
            print("O valor digitado pertence à sequência de Fibonacci.")
            return

        a = 0
        b = 1
        while b < numero:
            a, b = b, a + b

        if b == numero:
            print("O valor digitado pertence à sequência de Fibonacci.")
        else:
            print("O valor digitado NÃO pertence à sequência de Fibonacci.")

if __name__ == "__main__":
    fib = Fibonacci()
    fib.calcular()
