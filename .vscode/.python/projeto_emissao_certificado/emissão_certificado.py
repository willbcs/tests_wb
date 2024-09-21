import openpyxl
from PIL import Image, ImageDraw, ImageFont

workbook_alunos = openpyxl.load_workbook('C:/Users/Myrath/Desktop/Projetos_VSCode/.vscode/.python/projeto_emissao_certificado/planilha_alunos.xlsx')
aba_alunos = workbook_alunos['Sheet1']

for indice, linha in enumerate (aba_alunos.iter_rows(min_row = 2, values_only = True)):
    nome_professor = linha[0]
    nome_aluno = linha[1]
    data_conclusão = linha[2]
    carga_horaria = str(linha[3])
    data_emissao = linha[4].strftime('%d/%m/%Y')

    fonte_nome = ImageFont.truetype('C:/Users/Myrath/Desktop/Projetos_VSCode/.vscode/.python/projeto_emissao_certificado/tahomabd.ttf', 85)

    fonte_carga_horaria = ImageFont.truetype('C:/Users/Myrath/Desktop/Projetos_VSCode/.vscode/.python/projeto_emissao_certificado/tahoma.ttf', 38)
    
    fonte_emissao = ImageFont.truetype('C:/Users/Myrath/Desktop/Projetos_VSCode/.vscode/.python/projeto_emissao_certificado/tahoma.ttf', 20)
    
    fonte_geral = ImageFont.truetype('C:/Users/Myrath/Desktop/Projetos_VSCode/.vscode/.python/projeto_emissao_certificado/tahoma.ttf', 50)

    imagem = Image.open('C:/Users/Myrath/Desktop/Projetos_VSCode/.vscode/.python/projeto_emissao_certificado/Certificado_Padrao.jpg')
    
    escrever = ImageDraw.Draw(imagem)

    largura_imagem = 2000

    # Obtendo a delimitação do Nome do aluno
    bbox = escrever.textbbox((0, 0), nome_aluno, font=fonte_nome)
    largura_texto = bbox[2] - bbox[0]
    altura_texto = bbox[3] - bbox[1]
    x_centralizado = (largura_imagem - largura_texto) / 2

    escrever.text((x_centralizado, 477), nome_aluno, fill='black', font=fonte_nome)
    escrever.text((310, 900), nome_professor, fill='black', font=fonte_geral)
    escrever.text((1290, 895), data_conclusão, fill='black', font=fonte_geral)
    escrever.text((1109, 790), carga_horaria, fill='black', font=fonte_carga_horaria)
    escrever.text((1815, 1355), data_emissao, fill='black', font=fonte_emissao)

    imagem.save(f'C:/Users/Myrath/Desktop/Projetos_VSCode/.vscode/.python/projeto_emissao_certificado/Certificado {indice+1} - {nome_aluno}.png')