# src/services/gemini_service.py
import google.generativeai as genai
from src import config # Importa o módulo de configuração

# Configura a API Key globalmente para o SDK do Gemini
if config.GOOGLE_API_KEY:
    genai.configure(api_key=config.GOOGLE_API_KEY)
else:
    # Se não houver chave, o SDK não funcionará, então avisamos
    print("API Key do Gemini não configurada. O serviço Gemini não funcionará.")
    # Alternativamente, você pode levantar uma exceção ou ter um fallback

# Modelo padrão a ser usado, pode ser configurado ou passado como parâmetro
DEFAULT_MODEL_NAME = "gemini-1.5-flash-latest" # Ou "gemini-pro", "gemini-1.0-pro", etc.

def generate_text(prompt: str, model_name: str = DEFAULT_MODEL_NAME) -> str | None:
    """
    Gera texto usando o modelo Gemini especificado.

    Args:
        prompt (str): O prompt para enviar ao modelo.
        model_name (str, optional): O nome do modelo a ser usado.
                                    Defaults to DEFAULT_MODEL_NAME.

    Returns:
        str | None: O texto gerado pelo modelo, ou None em caso de erro.
    """
    if not config.GOOGLE_API_KEY:
        print("Não é possível gerar texto: API Key do Gemini não configurada.")
        return None

    try:
        model = genai.GenerativeModel(model_name)
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        print(f"Erro ao gerar texto com Gemini: {e}")
        # Poderia logar o erro aqui com mais detalhes
        return None

def start_chat_session(model_name: str = DEFAULT_MODEL_NAME):
    """
    Inicia uma sessão de chat com o modelo Gemini.

    Args:
        model_name (str, optional): O nome do modelo a ser usado.
                                    Defaults to DEFAULT_MODEL_NAME.
    Returns:
        genai.ChatSession | None: Uma sessão de chat ou None se a API Key não estiver configurada.
    """
    if not config.GOOGLE_API_KEY:
        print("Não é possível iniciar chat: API Key do Gemini não configurada.")
        return None
    try:
        model = genai.GenerativeModel(model_name)
        chat = model.start_chat(history=[])
        return chat
    except Exception as e:
        print(f"Erro ao iniciar sessão de chat com Gemini: {e}")
        return None

if __name__ == '__main__':
    # Pequeno teste se este arquivo for executado diretamente
    if config.GOOGLE_API_KEY:
        print("Testando gemini_service.py...")

        # Teste de geração simples
        prompt_simples = "Conte uma curiosidade sobre o universo."
        resposta_simples = generate_text(prompt_simples)
        if resposta_simples:
            print(f"\nPrompt: {prompt_simples}")
            print(f"Gemini: {resposta_simples}")
        else:
            print("Falha ao gerar texto simples.")

        # Teste de chat
        print("\nIniciando sessão de chat de teste...")
        chat_session = start_chat_session()
        if chat_session:
            primeira_mensagem = "Olá! Qual é a capital da França?"
            print(f"Você: {primeira_mensagem}")
            resposta_chat = chat_session.send_message(primeira_mensagem)
            print(f"Gemini: {resposta_chat.text}")

            segunda_mensagem = "E qual a sua principal atração turística?"
            print(f"Você: {segunda_mensagem}")
            resposta_chat = chat_session.send_message(segunda_mensagem)
            print(f"Gemini: {resposta_chat.text}")
        else:
            print("Falha ao iniciar sessão de chat.")
    else:
        print("gemini_service.py: API Key não configurada, não é possível testar.")