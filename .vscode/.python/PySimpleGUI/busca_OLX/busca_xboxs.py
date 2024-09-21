from PySimpleGUI import PySimpleGUI as sg
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from datetime import datetime
import pyperclip

sg.theme('Reddit')

def resultados_busca(dados): 
    layout = [
        [sg.Table(values=dados, headings=("Título", "Data", "Preço", "Link"), justification= 'Left', auto_size_columns = True, num_rows = 30, expand_x=True, enable_events=True, expand_y=True, key='-TABELA-', select_mode = sg.SELECT_MODE_BROWSE)],
        [sg.Button('Copiar Link'), sg.Button('Fechar')]
    ]
    janela = sg.Window("OLX - Resultados da busca | Xbox Series S", layout, size=(800,600)) 

    linha_selecionada = None

    while True:
        eventos, valores = janela.read()
        if eventos == sg.WINDOW_CLOSED or eventos == 'Fechar':
            break
        #Garantir que ele pegue linhas preenchidas
        if eventos == '-TABELA-':            
            if valores['-TABELA-']:
                linha_selecionada = valores['-TABELA-'][0]
            else: 
                None
        if eventos == 'Copiar Link' and linha_selecionada is not None:          
            link_copiado = dados[linha_selecionada][3]  # Índice 3 que é a coluna do link
            pyperclip.copy(link_copiado)
            sg.popup('Link copiado para a área de transferência!', keep_on_top=True) 
        
    janela.close()

resultado = []

driver = webdriver.Chrome()
driver.get('https://www.olx.com.br/games/consoles-de-video-game/estado-sp/baixada-santista-e-litoral-sul/santos?q=xbox%20series%20S')
sleep(6)

button_aceita = driver.find_element(By.XPATH, "//button[@id='adopt-accept-all-button']")
button_aceita.click()

valores = driver.find_elements(By.XPATH, "//h3[@data-ds-component ='DS-Text']")
titulos = driver.find_elements(By.XPATH, "//h2[@data-ds-component ='DS-Text']")
links = driver.find_elements(By.XPATH, "//a[@class ='olx-ad-card__title-link']")


for valor, titulo, link in zip(valores, titulos, links):
    valor_pronto = valor.text
    titulo_pronto = titulo.text
    link_pronto = link.get_attribute('href')
    data_atual = datetime.now().strftime('%d/%m/%Y')
    resultado.append([titulo_pronto, data_atual, valor_pronto, link_pronto])

driver.quit()

resultados_busca(resultado)
