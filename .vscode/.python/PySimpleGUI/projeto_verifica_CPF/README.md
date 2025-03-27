Projeto - Validador de CPF

📌 Visão Geral

Este projeto realiza a validação de CPFs a partir de uma planilha do Excel e exibe os resultados em uma interface gráfica.

📂 Estrutura do Projeto

projeto_verifica_CPF/
│-- cpf_clientes.xlsx  # Planilha contendo os CPFs a serem validados
│-- validacao_CPF.xlsx  # Planilha onde os resultados são armazenados
│-- automacao_CPF.py  # Script principal
│-- requirements.txt  # Dependências do projeto

🛠️ Tecnologias Utilizadas

Python 3.x

Selenium

OpenPyXL

PySimpleGUI

⚙️ Configuração e Instalação

Clone este repositório:

git clone https://github.com/willbcs/tests_wb.git
cd tests_wb/.vscode/.python/exercicios/projeto_verifica_CPF

Instale as dependências:

pip install -r requirements.txt

Certifique-se de ter o ChromeDriver compatível com sua versão do Google Chrome instalado.

🚀 Como Executar

Execute o script Python:

python automacao_CPF.py

O programa abrirá uma interface exibindo os CPFs e seus status de validação.

📌 Funcionalidades

Leitura de dados: O script lê nomes e CPFs da planilha cpf_clientes.xlsx.

Validação automática: Utiliza Selenium para acessar um site e validar cada CPF.

Registro dos resultados: Os CPFs validados são salvos na planilha validacao_CPF.xlsx.

Interface gráfica: Exibe os resultados da validação em uma tabela PySimpleGUI.

📄 Exemplo de Uso

O script lê a planilha e processa cada CPF automaticamente:

for linha in pagina_CPF.iter_rows(min_row=2, values_only=True):
    nome, cpf = linha
    campo_consulta = driver.find_element(By.XPATH, "//input[@id='cpf']")
    campo_consulta.clear()
    campo_consulta.send_keys(cpf)
    botao_consulta = driver.find_element(By.XPATH, "//button[@id='gerar']")
    botao_consulta.click()
    sleep(2)
    validacao = driver.find_element(By.XPATH, "//div[@id='resposta1']").text
    status = 'CPF Válido!' if 'válido' in validacao else 'CPF Inválido!'
    resultados.append([nome, cpf, status])

📬 Contato

Caso tenha dúvidas, entre em contato pelo e-mail: willbc.silva@gmail.com

Desenvolvido por 💻 William Bruno