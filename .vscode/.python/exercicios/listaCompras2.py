import os

class ListaDeCompras:
    def __init__(self):
        self.lista = []

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def inserir_item(self):
        while True:
            item = input('Digite um item para adicionar à lista (ou digite "sair" para voltar): ').strip()
            if item.lower() == 'sair':
                break
            elif item.isalpha():
                self.lista.append(item)
                self.clear_screen()
                print('Item adicionado à lista!\n')
            else:
                self.clear_screen()
                print('Por favor, digite apenas letras para o item.\n')

    def apagar_item(self):
        while True:
            self.clear_screen()
            self.listar_itens()

            if not self.lista:
                print('A lista está vazia.')
                return

            posicao = input('Digite o número do item que deseja apagar (ou digite "sair" para voltar): ').strip()
            if posicao.lower() == 'sair':
                break
            elif posicao.isdigit():
                posicao_num = int(posicao)
                if 1 <= posicao_num <= len(self.lista):
                    self.lista.pop(posicao_num - 1)
                    self.clear_screen()
                    print('Item removido da lista!\n')
                else:
                    print('Posição inválida, tente novamente.\n')
            else:
                print('Entrada inválida, por favor digite um número válido.\n')

    def listar_itens(self):
        self.clear_screen()
        print('Lista de Compras:')
        if self.lista:
            for i, item in enumerate(self.lista, start=1):
                print(f'{i}. {item}')
        else:
            print('A lista está vazia.')

    def iniciar(self):
        while True:
            print('Selecione uma opção:')
            print('[i]nserir  [a]pagar  [l]istar  [s]air\n')
            entrada = input().lower()

            if entrada == 'i':
                self.inserir_item()
            elif entrada == 'a':
                self.apagar_item()
            elif entrada == 'l':
                self.listar_itens()
            elif entrada == 's':
                print('Até logo!')
                break
            else:
                print('Opção inválida, por favor selecione uma das opções disponíveis.\n')

if __name__ == "__main__":
    app = ListaDeCompras()
    app.iniciar()
