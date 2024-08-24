sair = False
while sair is False:    
    valor_1 = input('Digite um número: ')
    if all(n.isdigit( ) for n in valor_1.split('.')):
        valor_2 = input('Digite outro número: ')
        if all(n.isdigit( ) for n in valor_2.split('.')):
            op = input('Digite um operador: ')
            op_v1 = '+-*/e'
            vlr_1 = float(valor_1)
            vlr_2 = float(valor_2)
            while op not in op_v1 or len(op) > 1:
                op = input("Isso não é um operador válido! Digite *, /, +, - ou e: ")
            else:
                if op == '+':
                    print(f'\nA soma de {vlr_1} e {vlr_2} é {vlr_1 + vlr_2}')
                elif op == '-':
                    print(f'\nA subtração de {vlr_1} e {vlr_2} é igual a {vlr_1 - vlr_2}')
                elif op == '*':
                    print(f'\nA multiplicação de {vlr_1} e {vlr_2} é igual a {vlr_1 * vlr_2}')
                elif op == 'e':
                    print(f'\nA resultado de {vlr_1} elevado a {vlr_2} é igual a {vlr_1 ** vlr_2}')       
                else:
                    if vlr_2 == 0:
                        print("\nDivisão por '0' não é válida!")
                    else:
                        print(f'A divisão de {vlr_1} e {vlr_2} é igual a {vlr_1 / vlr_2}')
        else:
            print("Isso não é um número!")
            continue
    else:
        print('Isso não é um número!')
        continue
    sair = input("\nAperte 's' para sair ou qualquer outra tecla para continuar:\n").lower().startswith('s')
    if sair is True:
        break 