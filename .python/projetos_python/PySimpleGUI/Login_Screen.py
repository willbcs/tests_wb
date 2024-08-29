from PySimpleGUI import PySimpleGUI as sg  # type: ignore

sg.theme('DarkTeal4')  # ou 'Reddit'

# Layout da Tela de Login
Layout = [ 
    [sg.Text('User:'), sg.Input(key='usuario', size=(20, 1))],
    [sg.Text('Password:'), sg.Input(key='senha', password_char='*', size=(20, 1))],
    [sg.Checkbox('Save?')],
    [sg.Button('Enter'), sg.Button('Close')]
]

# Layout da Tela de Boas-vindas
Layout2 = [
    [sg.Text('WELCOME, WILLIAM BRUNO!')],
    [sg.Button('Close')]
]

# Layout da Tela de Erro
Layout3 = [
    [sg.Text('WRONG PASSWORD OR USER!')],
    [sg.Button('Close')]
]

# Função para criar uma janela
def criar_janela(titulo, layout):
    return sg.Window(titulo, layout, finalize=True)

# Iniciar com a janela de login
janela = criar_janela('Login Screen', Layout)

while True:
    eventos, valores = janela.read()
    
    if eventos == sg.WINDOW_CLOSED or eventos == 'Close':
        break

    if eventos == 'Enter':
        if valores['usuario'] == 'willbc.silva' and valores['senha'] == '160489':
            janela.close()
            janela = criar_janela('Welcome', Layout2)
        else:
            janela.close()
            janela = criar_janela('ALERT!', Layout3)
    
    if eventos == 'Close' and janela.Title == 'ALERT!':
        janela.close()
        break

    if eventos == 'Close' and janela.Title == 'Welcome':
        janela.close()
        janela = criar_janela('Login Screen', Layout)

janela.close()