from PySimpleGUI import PySimpleGUI as sg
import math
import re

sg.theme('SystemDefault')

def Calcular(expressao):
    try:
        expressao = expressao.replace('√', '**0.5').replace('^2', '**2').replace('X', '*')
        resultado = eval(expressao)
        return resultado
    except: 
        return "Erro"

layout = [
    [sg.InputText('', key='-DISPLAY-', size=(18,1), justification='right',font=('Arial', 16, 'bold'), enable_events=True)],
    [sg.Button('√', size=(5,2)), sg.Button('^2', size=(5,2)), sg.Button('/', size=(5,2)), sg.Button('C', size=(5,2))],
    [sg.Button('7', size=(5,2)), sg.Button('8', size=(5,2)), sg.Button('9', size=(5,2)), sg.Button('X', size=(5,2))],
    [sg.Button('4', size=(5,2)), sg.Button('5', size=(5,2)), sg.Button('6', size=(5,2)), sg.Button('-', size=(5,2))],
    [sg.Button('1', size=(5,2)), sg.Button('2', size=(5,2)), sg.Button('3', size=(5,2)), sg.Button('+', size=(5,2))],
    [sg.Button('Fechar', size=(5,2)), sg.Button('0', size=(5,2)), sg.Button('.', size=(5,2)), sg.Button('=', size=(5,2), button_color=('white', 'red'))]
]

janela = sg.Window('Calculadora', layout)

while True:
    eventos, valores = janela.read()

    if eventos == sg.WINDOW_CLOSED or eventos == 'Fechar':
        break

    display = valores['-DISPLAY-']

    if eventos in '0123456789.':
        display += eventos
        janela['-DISPLAY-'].update(display)
    
    if eventos == '√' or eventos == '^2':
        display += eventos
        janela['-DISPLAY-'].update(display)

    if eventos == 'C':
        display = ''
        janela['-DISPLAY-'].update(display)

    if eventos in '+-/X':
        display += ' ' + eventos + ' '
        janela['-DISPLAY-'].update(display)

    if eventos == '=':
        resultado = Calcular(display)
        janela['-DISPLAY-'].update(resultado)
        display = resultado
    
    if eventos == '-DISPLAY-':
        display = re.sub(r'[^0-9.]', '', valores['-DISPLAY-'])
        janela['-DISPLAY-'].update(display)

janela.close()