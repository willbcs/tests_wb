🔍 Detecção de Objetos em Tempo Real com YOLOv8

📌 Visão Geral

Este projeto utiliza Python, OpenCV e YOLOv8 para realizar detecção de objetos em tempo real usando uma webcam USB.

🎥 Como Funciona?

O programa captura imagens da câmera em tempo real.

O modelo YOLOv8 analisa cada quadro e detecta objetos instantaneamente.

Objetos detectados são destacados com caixas delimitadoras e legendas.

O sistema pode rodar em CPU ou GPU (NVIDIA) para mais desempenho.

🛠️ Tecnologias Utilizadas

Python 🐍

OpenCV (Captura e processamento de imagem)

YOLOv8 (Detecção de objetos)

Torch (Framework de aprendizado de máquina)

📂 Estrutura do Projeto

📁 deteccao_objetos
│── 📁 modelos       # Modelos treinados YOLOv8
│── 📁 imagens       # Armazena imagens capturadas
│── 📁 scripts       # Códigos principais do projeto
│   │── captura.py   # Captura de vídeo
│   │── detecao.py   # Detecção de objetos
│── requirements.txt # Dependências do projeto
│── main.py         # Arquivo principal

🚀 Instalação e Execução

1️⃣ Clonar o repositório

git clone https://github.com/willbcs/tests_wb.git
cd tests_wb/.vscode/.python/deteccao_objetos

2️⃣ Instalar dependências

pip install -r requirements.txt

3️⃣ Executar o projeto

Apenas visualizar a câmera:
python scripts/captura.py

Rodar a detecção de objetos:
python scripts/detecao.py

Rodar tudo pelo main.py:
python main.py

🔥 Recursos e Melhorias Futuras

✅ Captura e exibição de vídeo em tempo real
✅ Detecção de objetos com YOLOv8
✅ Pode rodar offline
🔜 Suporte para gravação de vídeo
🔜 Melhorias na interface gráfica

🔗 Autor: William Bruno Carlos Silva
📅 Data: Março de 2025
📜 Licença: MIT License
