import os

def verifica_numero(mensagem):
    while True:
        numero = input(mensagem)
        if all(n.isdigit() for n in numero.split('.')) and numero.count('.') <= 1:
            return float(numero)
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\nIsso não é um número válido! Digite um número inteiro ou decimal.\n")

def verifica_operador():
    operadores_validos = "+-*/e"
    while True:
        operador = input("Digite um operador (*, /, +, -, e para exponenciação): ").strip()
        if operador in operadores_validos and len(operador) == 1:
            return operador
        print("\nIsso não é um operador válido! Digite *, /, +, -, ou e.\n")

def encerrar(mensagem):
    while True:
        sair = input(mensagem).strip().lower()
        if sair in ["s", "c"]:
            return sair == "s"
        print("Inválido! Aperte [S] para sair ou [C] para continuar.\n")

def calculadora():
    while True:
        valor_1 = verifica_numero("Digite um número: ")
        valor_2 = verifica_numero("Digite outro número: ")
        operador = verifica_operador()

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

        if encerrar("\nAperte [S] para sair ou [C] para continuar: "):
            break

if __name__ == "__main__":
    calculadora()
