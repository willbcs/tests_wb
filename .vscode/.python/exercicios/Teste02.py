h = input('Digite o horário: ')
if h.isdigit():
    hint = int(h)
    if hint <= 23 and hint >= 0:
        m = input('Digite os minutos: ')
        if m.isdigit():
            mint = int(m)
            if mint <= 59 and mint >= 0:
                if hint >= 0 and hint <= 11 and mint <= 59:
                    print(f'Bom dia! Agora são {hint} horas e {mint} minutos!')
                elif hint >= 12 and hint <= 17 and mint <= 59:
                    print(f'Boa tarde! Agora são {hint} horas e {mint} minutos!')
                elif hint >= 18 and hint <= 23 and mint <= 59:
                    print(f'Boa noite! Agora são {hint} horas e {mint} minutos!')
                else:
                    print("Não é um horário válido!")
            else:
                print('Não é um valor correto para minutos')
        else:
            print('Por favor, digite apenas números')
    else:
        print('Esse não é um valor aceitável para horas!')
else:
    print('Por favor, digite apenas números')