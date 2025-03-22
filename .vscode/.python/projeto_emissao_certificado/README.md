Projeto - Emissão de Certificados

Este projeto gera certificados personalizados a partir de uma imagem padrão e de uma planilha de alunos.

📂 Estrutura do Projeto

📂 projeto_emissao_certificado/
│-- Certificado_Padrao.jpg  # Imagem base do certificado
│-- emissao_certificado.py  # Script principal
│-- planilha_alunos.xlsx  # Planilha contendo os dados dos alunos
│-- tahoma.ttf  # Fonte utilizada no certificado
│-- tahomabd.ttf  # Fonte em negrito utilizada no certificado

🛠️ Tecnologias Utilizadas

Python 3.x

OpenPyXL

Pillow (PIL)

⚙️ Configuração e Instalação

Clone este repositório:

git clone https://github.com/seu-repositorio.git
cd projeto_emissao_certificado

Instale as dependências:

pip install openpyxl pillow

Certifique-se de que os arquivos necessários (imagem base, planilha e fontes) estão no diretório correto.

🚀 Como Executar

Execute o script Python:

python emissao_certificado.py

Os certificados gerados serão salvos no mesmo diretório do projeto.

📌 Funcionalidades

Leitura de dados: O script lê nomes de professores, alunos, datas e carga horária de um arquivo Excel.

Geração de certificados: Insere as informações extraídas na imagem do certificado.

Salvamento automático: Cada certificado é salvo em formato PNG com o nome do aluno.

📬 Contato

Caso tenha dúvidas, entre em contato pelo e-mail: willbc.silva@gmail.com

Desenvolvido por 💻 por William Bruno

