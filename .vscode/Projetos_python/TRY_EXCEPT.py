while True:
    try:
        numero_1 = float(input("Digite qualquer número: "))
        break
    except ValueError:
        print("Inválido!")
    
while True:
    try:
        numero_2 = float(input("Digite qualquer outro número: "))
        break
    except ValueError:
        print("Inválido!")
    
if numero_1 == numero_2:
    print("Os números são iguais")

else:
    mensagem = f'Em ordem crescente os números são {numero_1} e {numero_2}' if numero_1 > numero_2 else f'Em ordem crescente os números são {numero_2} e {numero_1}'
    print(mensagem)

