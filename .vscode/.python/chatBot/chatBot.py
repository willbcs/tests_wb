import os
import requests
from dotenv import load_dotenv

# Carrega as variáveis do .env
load_dotenv()

# Obtém a chave da API do arquivo .env
HUGGINGFACE_API_KEY = os.getenv("API_KEY")
API_URL = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.1"
HEADERS = {"Authorization": f"Bearer {HUGGINGFACE_API_KEY}"}

conversation_history = []  # Para manter o contexto das interações

def chat_with_jonny(prompt):
    global conversation_history

    # Adiciona apenas a nova pergunta ao histórico
    conversation_history.append(f"Você: {prompt}")

    # Mantém apenas as últimas 4 interações (2 perguntas e 2 respostas)
    history_text = "\n".join(conversation_history[-4:])

    formatted_prompt = (
        "Você é o Jonny, um assistente de IA útil. Responda apenas à última pergunta do usuário de forma direta.\n"
        "Não continue o diálogo, apenas responda ao que foi perguntado.\n"
        "---\n"
        f"{history_text}\n"
        "Jonny:"
    )

    payload = {
        "inputs": formatted_prompt,
        "parameters": {
            "temperature": 0.5,
            "max_new_tokens": 150,
            "return_full_text": False,
            "do_sample": True,
            "stop_sequences": ["\nVocê:"]
        }
    }

    try:
        response = requests.post(API_URL, headers=HEADERS, json=payload)
        response.raise_for_status()
        output = response.json()

        response_text = ""
        if isinstance(output, list) and len(output) > 0:
            response_text = output[0].get("generated_text", "").strip()
            response_text = response_text.split("\n")[0]
        elif isinstance(output, dict):
            response_text = output.get("generated_text", "").strip()
            response_text = response_text.split("\n")[0]

        if not response_text:
            resposta_final = "Desculpe, não entendi. Poderia reformular a pergunta?"
        else:
            resposta_final = response_text

        # Adiciona a resposta ao histórico
        conversation_history.append(f"Jonny: {resposta_final}")

        return resposta_final
    except requests.exceptions.RequestException as e:
        return f"Ops! Houve um erro: {str(e)}"

def get_user_input():
    try:
        return input("\nVocê: ").strip()
    except (EOFError, OSError):
        return "sair"

def main():
    print("Bem-vindo ao Chat Jonny!")
    print("Digite 'sair' para encerrar o programa.\n")

    while True:
        user_input = get_user_input()
        if user_input.lower() == "sair":
            print("\nJonny: Até logo! Foi ótimo conversar com você! 👋")
            break

        response = chat_with_jonny(user_input)
        print(f"\nJonny: {response}")

if __name__ == "__main__":
    main()
