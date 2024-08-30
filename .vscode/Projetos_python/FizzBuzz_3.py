n = input('Digite um número: ')
if n.isdigit():
    n_inteiro = int(n)
    for n_inteiro in range(1,n_inteiro + 1):
        if n_inteiro % 3 == 0 and n_inteiro % 5 == 0:
            print('FizzBuzz')
        elif n_inteiro % 3 == 0:
            print('Fizz')
        elif n_inteiro % 5 == 0:
            print('Buzz')
        else:
            print(n_inteiro)
else:
    print('Isso não é um número')
    quit()