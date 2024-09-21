import re
from PySimpleGUI import PySimpleGUI as sg

sg.theme('Reddit')

def tamanho_cpf(cpf):
    formato_cpf = cpf
    if len(formato_cpf) == 11:
        return formato_cpf
    else:
        return None

def Validar_penultimo_digito(cpf):
    nove_digitos = cpf[:9]
    contadord1 = 10
    resultado = 0
    for numero in nove_digitos:
        resultado += int(numero) * contadord1
        contadord1 -= 1
    return 0 if (resultado * 10) % 11 > 9 else (resultado * 10) % 11
        
def Validar_ultimo_digito(cpf):
    nove_digitos = cpf[:10]
    contadord2 = 11
    resultado = 0
    for numero in nove_digitos:
        resultado += int(numero) * contadord2
        contadord2 -= 1
    return 0 if (resultado * 10) % 11 > 9 else (resultado * 10) % 11

def Validador(cpf):
    formato_cpf = tamanho_cpf(cpf)
    if formato_cpf is not None:
        penultimo_digito_calculado = Validar_penultimo_digito(cpf)
        penultimo_digito_original = int(cpf[9])
        ultimo_digito_calculado = Validar_ultimo_digito(cpf)
        ultimo_digito_original = int(cpf[10])

        sucesso = (penultimo_digito_calculado == penultimo_digito_original) and (ultimo_digito_calculado == ultimo_digito_original)
       
        mensagem = f'O CPF informado é VÁLIDO!' if sucesso else f'O CPF informado é INVÁLIDO!'

        return mensagem, sucesso
        # A parte superior também poderia ter sido escrita assim:
                
        # if (penultimo_digito_calculado == penultimo_digito_original) and (ultimo_digito_calculado == ultimo_digito_original):
        #     return f'O CPF informado é VÁLIDO!', True
        # else:
        #     return f'O CPF informado é INVÁLIDO!', False
    else:
        return f'O CPF está em formato incorreto!', False

def main():
    Layout = [
        [sg.Text('', size=(1,1))],
        [sg.Text('Digite o CPF:'), sg.Input(key = 'cpf', size = (25,1), enable_events = True)], #Enable events serve para habilitar uma geração de eventos. No caso coloquei aqui porque vou remover quaisquer caracteres no preenchimento que não sejam números.
        [sg.Text('', size=(1,1))],
        [sg.Button('Validar'), sg.Button('Fechar')],
        [sg.Text('', size=(1,1))],
        [sg.Text('', size=(30,1), key='resposta')]    
    ]

    janela = sg.Window('Validador de CPF', Layout)

    while True:
        eventos, valores = janela.read()
        if eventos == sg.WINDOW_CLOSED or eventos == 'Fechar':
            break
        if eventos == 'Validar':
            cpf = valores['cpf']
            mensagem, sucesso = Validador(cpf)
            janela['resposta'].update(mensagem, text_color='green' if sucesso else 'red', font=('Default', 10, 'bold')) # De acordo com o que vier de 'mensagem' ele retorna ela em uma cor específica. 
        if eventos == 'cpf':
            # Permitir apenas números ao digitar
            cpf = re.sub(r'[^\d]', '', valores['cpf'])
            janela['cpf'].update(cpf)
            
    janela.close()

if __name__== '__main__':
    main()