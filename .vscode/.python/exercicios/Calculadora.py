import os

class Calculadora:
    def __init__(self):
        self.operadores_validos = "+-*/e"
        
    def verifica_numero(self, mensagem):
        while True:
            numero = input(mensagem)
            if all(n.isdigit() for n in numero.split('.')) and numero.count('.') <= 1:
                return float(numero)
            os.system('cls' if os.name == 'nt' else 'clear')
            print("\nIsso não é um número válido! Digite um número inteiro ou decimal.\n")

    def verifica_operador(self):
        while True:
            operador = input("Digite um operador (*, /, +, -, e para exponenciação): ").strip()
            if operador in self.operadores_validos and len(operador) == 1:
                return operador
            print("\nIsso não é um operador válido! Digite *, /, +, -, ou e.\n")

    def encerrar(self, mensagem):
        while True:
            sair = input(mensagem).strip().lower()
            if sair in ["s", "c"]:
                return sair == "s"
            print("Inválido! Aperte [S] para sair ou [C] para continuar.\n")

    def calcular(self):
        while True:
            valor_1 = self.verifica_numero("Digite um número: ")
            valor_2 = self.verifica_numero("Digite outro número: ")
            operador = self.verifica_operador()

            os.system('cls' if os.name == 'nt' else 'clear')

            if operador == '+':
                resultado = valor_1 + valor_2
                print(f"A soma de {valor_1} e {valor_2} é {resultado}")
            elif operador == '-':
                resultado = valor_1 - valor_2
                print(f"A subtração de {valor_1} e {valor_2} é {resultado}")
            elif operador == '*':
                resultado = valor_1 * valor_2
                print(f"A multiplicação de {valor_1} e {valor_2} é {resultado}")
            elif operador == 'e':
                resultado = valor_1 ** valor_2
                print(f"O resultado de {valor_1} elevado a {valor_2} é {resultado}")
            elif operador == '/':
                if valor_2 == 0:
                    print("Erro: Divisão por zero não é válida!")
                else:
                    resultado = valor_1 / valor_2
                    print(f"A divisão de {valor_1} por {valor_2} é {resultado}")

            if self.encerrar("\nAperte [S] para sair ou [C] para continuar: "):
                break

if __name__ == "__main__":
    calc = Calculadora()
    calc.calcular()
