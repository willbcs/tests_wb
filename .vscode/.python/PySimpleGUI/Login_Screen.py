from PySimpleGUI import PySimpleGUI as sg  
sg.theme('Reddit')  # ou 'DarkTeal4'

# Layout da Tela para Inserir o CPF
Layout = [ 
    [sg.Text('User:'), sg.Input(key='usuario', size=(20, 1))],
    [sg.Text('Password:'), sg.Input(key='senha', password_char='*', size=(20, 1))],
    [sg.Checkbox('Save?')],
    [sg.Text('', size=(1,1))],
    [sg.Button('Enter'), sg.Button('Close')],   
    [sg.Text('', size=(30,1), font=('Default', 10, 'bold') , key='resposta')]
]

# Layout da Tela de Boas-vindas
Layout2 = [
    [sg.Text('Bem-vindo WILLIAM BRUNO!', size=(30,1), font=('Default', 10, 'bold'))],
    [sg.Text('', size=(1,1))],
    [sg.Button('Close')]    
]

# Criar uma janela
janela = sg.Window('Login Screen', Layout, finalize=True)

while True:
    eventos, valores = janela.read()
    
    if eventos == sg.WINDOW_CLOSED or eventos == 'Close':
        break

    if eventos == 'Enter':
        if valores['usuario'] == 'willbc.silva' and valores['senha'] == '160489':
            janela.close()
            janela = sg.Window('Welcome', Layout2, finalize=True)        
        else:
            janela['resposta'].update('Usuário ou senha incorretos!', text_color = 'red')    

janela.close()