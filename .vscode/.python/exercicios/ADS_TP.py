import os

class Fibonacci:
    def verifica_digito(self, mensagem):
        while True:
            termos = input(mensagem)
            try:
                termos = int(termos)
                if termos <= 0:
                    print("\nPor favor, insira um número maior que zero.\n")
                else:
                    return termos
            except ValueError:
                print("\nCaracteres inválidos foram digitados! Por favor, insira um número inteiro.\n")

    def encerrar(self):
        sair = input("\nDeseja encerrar o programa? (s/n): ").strip().lower()
        while sair not in ('s', 'n'):
            print("\nOpção inválida! Por favor, digite 's' para sim ou 'n' para não.")
            sair = input("Deseja encerrar o programa? (s/n): ").strip().lower()
        return sair == 's'

    def gerar_sequencia(self, termos):
        a, b = 1, 1
        sequencia = [a]
        if termos > 1:
            sequencia.append(b)
            for _ in range(2, termos):
                a, b = b, a + b
                sequencia.append(b)
        return sequencia

    def calcula(self):
        while True:
            termos = self.verifica_digito("Digite a quantidade de termos da sequência de Fibonacci que deseja visualizar: ")
            sequencia = self.gerar_sequencia(termos)
            print(f"\nSequência de Fibonacci com {termos} termo(s):")
            print(", ".join(map(str, sequencia)))
            if self.encerrar():
                print("\nEncerrando o programa...")
                break
            else:
                os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == "__main__":
    fib = Fibonacci()
    fib.calcula()