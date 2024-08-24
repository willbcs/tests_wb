def eh_numero(valor):
    while True:
        numero = input(valor)
        try: 
            return int(numero)
        except ValueError:
            print("Caracteres inválidos foram digitados: ")

def fizzBuzz(n):
    for n in range(1,n+1):
        if n % 3 == 0 and n % 5 == 0:
            print('FizzBuzz')
        elif n % 3 == 0:
            print('Fizz')
        elif n % 5 == 0:
            print('Buzz')
        else:
            print(n)


if __name__ == '__main__': 
    n = eh_numero('Digite um número: ')
    fizzBuzz(n)