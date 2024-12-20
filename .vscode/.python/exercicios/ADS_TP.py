def verifica_digito(mensagem):
    while True:
        termos = input(mensagem)
        try:
            return int(termos)
        except ValueError:
            print("\nCaracteres inválidos foram digitados!\n")

def fibonacci():
    a= 1; b=1
    while True:
        termos = verifica_digito("Digite a quantidade de termos da sequência de Fibonacci que deseja visualizar: ")
        
        if termos == 1:
            print(f"\nSequência de Fibonacci com 1 termo:\n{a}\n")
        elif termos == 2:
            print(f"\nSequência de Fibonacci com 2 termos:\n{a}, {b}\n")
        else:
            print(f"\nSequência de Fibonacci com {termos} termos:")
            print(f"{a},", end=" ")
            print(f"{b},", end=" ")
            for i in range(2, termos):
                next_term = a + b
                print(next_term, end=" ")
                a, b = b, next_term # Isso é o mesmo que a = b; b = next_therm
            print("\n")
        break
if __name__== "__main__":
    fibonacci()