import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def insert_item():
    while True:
        item = input('Digite um item para adicionar à lista (ou digite "sair" para voltar): ').strip()
        if item.lower() == 'sair':
            break
        elif item.isalpha():
            listaCompras.append(item)
            clear_screen()
            print('Item adicionado à lista!\n')
        else:
            clear_screen()
            print('Por favor, digite apenas letras para o item.\n')
            continue

def delete_item():
    while True:
        clear_screen()
        print('Lista de Compras:')
        for i, item in enumerate(listaCompras, start=1):
            print(f'{i}. {item}')
        if not listaCompras:
            print('A lista está vazia.')
        posicao = input('Digite o número do item que deseja apagar (ou digite "sair" para voltar): ').strip()
        if posicao.lower() == 'sair':
            break
        elif posicao.isdigit():
            posicao_num = int(posicao)
            if 1 <= posicao_num <= len(listaCompras):
                listaCompras.pop(posicao_num - 1)
                clear_screen()
                print('Item removido da lista!\n')
            else:
                print('Posição inválida, tente novamente.\n')
        else:
            print('Entrada inválida, por favor digite um número válido.\n')

def list_items():
    clear_screen()
    print('Lista de Compras:')
    for item in listaCompras:
        print(item)
    if not listaCompras:
        print('A lista está vazia.')

listaCompras = []

while True:
    print('\nSelecione uma opção:')
    print('[i]nserir  [a]pagar  [l]istar  [s]air\n')
    entrada = input().lower()

    if entrada == 'i':
        insert_item()
    elif entrada == 'a':
        delete_item()
    elif entrada == 'l':
        list_items()
    elif entrada == 's':
        print('Até logo!')
        break
    else:
        print('Opção inválida, por favor selecione uma das opções disponíveis.\n')