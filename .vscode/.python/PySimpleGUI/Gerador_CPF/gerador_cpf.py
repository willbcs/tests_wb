from PySimpleGUI import PySimpleGUI as sg
import pyperclip
import random

sg.theme('SystemDefault')

def gerar_nove_digitos():
    nove_numeros = random.choices(range(10), k=9)
    return nove_numeros

def criar_penultimo_digito():
    nove_digitos = gerar_nove_digitos()
    contadord1 = 10
    resultado = 0
    for numero in nove_digitos:
        resultado += int(numero) * contadord1
        contadord1 -= 1
    
    penultimo_digito = 0 if (resultado * 10) % 11 > 9 else (resultado * 10) % 11
    nove_digitos.append(penultimo_digito)
    
    return nove_digitos
        
def criar_ultimo_digito():
    dez_digitos = criar_penultimo_digito()
    contadord2 = 11
    resultado = 0
    for numero in dez_digitos:
        resultado += int(numero) * contadord2
        contadord2 -= 1
    ultimo_digito = 0 if (resultado * 10) % 11 > 9 else (resultado * 10) % 11
    dez_digitos.append(ultimo_digito)
    return dez_digitos

def formato_cpf(cpf_lista):
    cpf_formato = ''.join(map(str, cpf_lista))
    return f'{cpf_formato[:3]}.{cpf_formato[3:6]}.{cpf_formato[6:9]}-{cpf_formato[9:]}'

def main():
    Layout = [
        [sg.Text('', size=(1,1))],
        [sg.Text('CPF:'), sg.Input('', key = 'resposta', size = (25,1), disabled= True)], #Enable events serve para habilitar uma geração de eventos. No caso coloquei aqui porque vou remover quaisquer caracteres no preenchimento que não sejam números.
        [sg.Text('', size=(1,1))],
        [sg.Button('Gerar CPF'), sg.Button('Copiar CPF'), sg.Button('Fechar')],
        [sg.Text('', size=(1,1))]
            
    ]

    janela = sg.Window('Gerador de CPF', Layout)

    while True:
        eventos, valores = janela.read()
        if eventos == sg.WINDOW_CLOSED or eventos == 'Fechar':
            break
        if eventos == 'Gerar CPF':
            cpf_lista = criar_ultimo_digito()
            cpf_formatado = formato_cpf(cpf_lista) #Isso transforma lista em string
            janela['resposta'].update(cpf_formatado, text_color='blue', font=('Default', 10, 'bold'))
        if eventos == 'Copiar CPF':
            copiar_cpf = janela['resposta'].get()
            pyperclip.copy(copiar_cpf)
            sg.popup('CPF copiado para a área de transferância!', keep_on_top=True)
            
    janela.close()

if __name__== '__main__':
    main()