import PySimpleGUI as sg
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

sg.theme('Reddit')

def exportar_PDF(tarefas):
    # Cria o documento PDF
    pdf_file = "C:\\Users\\Myrath\\Documentos\\Tarefas.pdf"
    doc = SimpleDocTemplate(pdf_file, pagesize=letter)

    # Cabeçalhos da tabela
    headers = ['Título', 'Status', 'Prioridade']
    
    # Monta os dados da tabela
    data = [headers] + tarefas  # Adiciona cabeçalhos e os dados

    # Cria a tabela
    table = Table(data)

    # Estilo da tabela
    style = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),  # Cor de fundo do cabeçalho
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),  # Centraliza o texto
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),  # Títulos em negrito
        ('FONTSIZE', (0, 0), (-1, 0), 14),  # Tamanho da fonte do cabeçalho
        ('FONTSIZE', (0, 1), (-1, -1), 12),  # Tamanho da fonte do restante
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ])
    table.setStyle(style)

    # Ajusta a largura das colunas
    column_widths = [200, 100, 100]  # Ajuste conforme necessário
    table._argW = column_widths

    # Estilo do cabeçalho
    styles = getSampleStyleSheet()
    header_style = styles['Title']  # Usa um estilo de título padrão
    header_style.fontSize = 18  # Aumenta o tamanho da fonte
    header_style.alignment = 1  # Centraliza o texto

    # Cria o cabeçalho
    header = Paragraph("Lista de Tarefas", header_style)

    # Constrói o PDF
    elements = [header, table]  # Adiciona o cabeçalho antes da tabela
    doc.build(elements)

    sg.popup('Tarefas exportadas para PDF com sucesso!')

tarefas = []
status = ['Em andamento', 'Não iniciado', 'Concluído']
prioridades = ['Alta', 'Média', 'Baixa']

font_titulo = ('Helvetica', 12, 'bold')  # Fonte para os títulos
font_input = ('Helvetica', 12)            # Fonte para os inputs

# Layout do aplicativo
layout = [
    [sg.Text('Tarefas', font=font_titulo, relief=sg.RELIEF_RIDGE,), sg.Input(key='-TAREFA-', size=(30, 1))],
    [sg.Text('Status', font=font_titulo, relief=sg.RELIEF_RIDGE,), sg.Combo(status, key='-STATUS-', readonly=True, size=(15, 1))],
    [sg.Text('Prioridade', font=font_titulo, relief=sg.RELIEF_RIDGE,), sg.Combo(prioridades, key='-PRIORIDADE-', size=(15, 1))],
    [sg.Text('')],  
    [sg.Button('Inserir', font= ('Default',10, 'bold')), sg.Button('Remover', font= ('Default',10, 'bold')), sg.Button('Exportar PDF', font= ('Default',10, 'bold'))],
    [sg.Text('')],  
    [sg.Table(values=tarefas, headings=("Título", "Status", "Prioridade"), 
              justification='left', key='-LISTA-', 
              enable_events=True, 
              auto_size_columns=False, 
              col_widths=[15, 10, 10],  
              size=(60, 15))],  
    [sg.Text('')],  
    [sg.Button('Fechar', size=(10, 1), font= ('Default',10, 'bold'))]  
]
janela = sg.Window('Gerenciador de Tarefas', layout, size=(350, 500), grab_anywhere=True, finalize = True)
janela.move_to_center()

while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED or eventos == 'Fechar':
        break

    elif eventos == 'Inserir':
        titulo = valores['-TAREFA-']
        stats = valores['-STATUS-']
        prioridade = valores['-PRIORIDADE-']
        if titulo and stats and prioridade:
            tarefas.append([titulo, stats, prioridade])
            janela['-LISTA-'].update(values=tarefas)
            janela['-TAREFA-'].update('')  
            janela['-STATUS-'].update('')  
            janela['-PRIORIDADE-'].update('')
        else:
            sg.popup('Preencha todos os campos!', title='Aviso!')

    elif eventos == 'Remover':
        selecao = valores['-LISTA-']
        if selecao:
            # Obter a linha selecionada e remover a tarefa correspondente
            tarefa_remover = tarefas[selecao[0]]
            tarefas.remove(tarefa_remover)
            janela['-LISTA-'].update(values=tarefas)
        else:
            sg.popup('Nenhuma tarefa selecionada para remover.', title='Aviso!')

    elif eventos == 'Exportar PDF':
        exportar_PDF(tarefas) if tarefas else sg.popup('Não há tarefas para exportar!', title='Aviso!')

janela.close()
