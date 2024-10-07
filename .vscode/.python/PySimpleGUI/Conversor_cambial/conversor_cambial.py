from PySimpleGUI import PySimpleGUI as sg
import requests
import re

sg.theme('Systemdefault')

API_KEY = '567c400e40df803fa1d650f5'
BASE_URL = 'https://v6.exchangerate-api.com/v6/567c400e40df803fa1d650f5/latest/'

    
def obter_conversao():
    url = BASE_URL + 'BRL'
    resposta = requests.get(url)
    dados = resposta.json()
    
    if resposta.status_code == 200 and dados['result'] == 'success':
        usd = dados['conversion_rates']['USD']
        eur = dados['conversion_rates']['EUR']
        gbp = dados['conversion_rates']['GBP']
        jpy = dados['conversion_rates']['JPY']
        aud = dados['conversion_rates']['AUD']
        cad = dados['conversion_rates']['CAD']
        cny = dados['conversion_rates']['CNY']
        chf = dados['conversion_rates']['CHF']
        ars = dados['conversion_rates']['ARS']
        
        cambios = [usd, eur, gbp, jpy, aud, cad, cny, chf, ars]

        return cambios 
    else:
        return None
    
layout = [
    
    [sg.Text('Digite o valor em reais:', relief = sg.RELIEF_RIDGE, font=('Default', 10, 'bold'), justification='center')],

    [sg.Input('', key='valor_reais', size=(21,1), enable_events=True), sg.Button('Converter'), sg.Button('Fechar')],
    [sg.Text('', size=(1,1))],

    [sg.Text('Dólar US:', relief = sg.RELIEF_RIDGE, font = ('Default', 10, 'bold'), justification='center', size=(15,1)), sg.Text('', key = '-DOLAR-', font = ('Default', 10, 'bold'))],
    
    [sg.Text('EURO:', relief = sg.RELIEF_RIDGE, font = ('Default', 10, 'bold'), justification='center', size=(15,1)), sg.Text('', key = '-EURO-', font = ('Default', 10, 'bold'))],
    
    [sg.Text('Libra ENG:', relief = sg.RELIEF_RIDGE, font = ('Default', 10, 'bold'), justification='center', size=(15,1)), sg.Text('', key = '-LIBRA-', font = ('Default', 10, 'bold'))],
    
    [sg.Text('Iene JPN:', relief = sg.RELIEF_RIDGE, font = ('Default', 10, 'bold'), justification='center', size=(15,1)), sg.Text('', key = '-IENE-', font = ('Default', 10, 'bold'))],
    
    [sg.Text('Dólar AUS:', relief = sg.RELIEF_RIDGE, font = ('Default', 10, 'bold'), justification='center', size=(15,1)), sg.Text('', key = '-DOLARAUS-', font = ('Default', 10, 'bold'))],
    
    [sg.Text('Dólar CND:', relief = sg.RELIEF_RIDGE, font = ('Default', 10, 'bold'), justification='center', size=(15,1)), sg.Text('', key = '-DOLARCND-', font = ('Default', 10, 'bold'))],
    
    [sg.Text('Yuan CHI:', relief = sg.RELIEF_RIDGE, font = ('Default', 10, 'bold'), justification='center', size=(15,1)), sg.Text('', key = '-YUAN-', font = ('Default', 10, 'bold'))],
    
    [sg.Text('Franco SUI:', relief = sg.RELIEF_RIDGE, font = ('Default', 10, 'bold'), justification='center', size=(15,1)), sg.Text('', key = '-FRANCO-', font = ('Default', 10, 'bold'))],
    
    [sg.Text('Peso ARG:', relief = sg.RELIEF_RIDGE, font = ('Default', 10, 'bold'), justification='center', size=(15,1)), sg.Text('', key = '-PESO-', font = ('Default', 10, 'bold'))],
    [sg.Text('', size=(1,1))]

]

janela = sg.Window("Conversor cambial", layout, grab_anywhere=True, finalize=True)

while True:
    eventos, valores = janela.read()
    if eventos == 'Fechar' or eventos == sg.WINDOW_CLOSED:
        break

    if eventos == 'Converter':
        try:
            valor_real = float(valores['valor_reais'])
            cambio = obter_conversao()

            if cambio is not None:
                janela['-DOLAR-'].update(f'US$ {cambio[0] * valor_real:.2f}')
                janela['-EURO-'].update(f'€ {cambio[1] * valor_real:.2f}')
                janela['-LIBRA-'].update(f'£ {cambio[2] * valor_real:.2f}')
                janela['-IENE-'].update(f'¥ {cambio[3] * valor_real:.2f}')
                janela['-DOLARAUS-'].update(f'AU$ {cambio[4] * valor_real:.2f}')
                janela['-DOLARCND-'].update(f'CA$ {cambio[5] * valor_real:.2f}')
                janela['-YUAN-'].update(f'¥ {cambio[6] * valor_real:.2f}')
                janela['-FRANCO-'].update(f'CHF {cambio[7] * valor_real:.2f}')
                janela['-PESO-'].update(f'$ {cambio[8] * valor_real:.2f}')
            else:
                sg.popup('Erro de comunicação. Tente novamente mais tarde.')

        except ValueError:
            sg.popup('Por favor, digite um valor válido!')

    if eventos == 'valor_reais':
            # Permitir apenas números ao digitar
            valor_limpo = re.sub(r'[^0-9.]', '', valores['valor_reais'])
            janela['valor_reais'].update(valor_limpo)

janela.close()