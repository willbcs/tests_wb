quantidade_termos = input("Digite a quantidade de termos da sequência de Fibonacci que deseja visualizar: ")
a = 1; b = 1
while not quantidade_termos.isdigit() or not int(quantidade_termos) > 0:
    quantidade_termos = input("Valor inválido! \nDigite a quantidade de termos da sequência de Fibonacci que deseja visualizar: ")
termos = int(quantidade_termos)
if termos == 1:
    print("Sequência de Fibonacci com 1 termo:", a)
elif termos == 2:
    print("Sequência de Fibonacci com 2 termos:", a, b)
else:
    print(f'Sequência de Fibonacci com {termos} termos:')
    print(a, end=" ")
    print(b, end=" ")
    for i in range(2, termos):
        next_term = a + b
        print(next_term, end=" ")
        a, b = b, next_term # Isso é o mesmo que a = b; b = next_therm
        