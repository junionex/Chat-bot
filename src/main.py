# src/main.py
from src.services import gemini_service
from src import config
from colorama import Fore, Back, Style, init

def run_application():
    """Função principal para rodar a aplicação de exemplo."""
    print("Bem-vindo ao seu projeto com API Gemini!")

    if not config.GOOGLE_API_KEY:
        print("Por favor, configure sua GOOGLE_API_KEY no arquivo .env antes de continuar.")
        return

    # Exemplo 1: Geração de texto simples
    print("\n--- Exemplo de Geração de Texto Simples ---")
    prompt_ideia = "Me dê 3 ideias de nome para um aplicativo de receitas veganas."
    print(f"Enviando prompt: '{prompt_ideia}'")
    ideias = gemini_service.generate_text(prompt_ideia)

    if ideias:
        print("\nIdeias do Gemini:")
        print(ideias)
    else:
        print("Não foi possível obter ideias do Gemini.")

    # Exemplo 2: Sessão de Chat
    print("\n--- Exemplo de Sessão de Chat Interativo ---")
    chat_session = gemini_service.start_chat_session()

    if chat_session:
        print("Sessão de chat iniciada. Digite 'sair' para terminar.")
        while True:
            user_input = input(Fore.GREEN +"Você: ")
            if user_input.lower() == 'sair':
                print("Encerrando chat...")
                break

            if not user_input.strip(): # Ignora entradas vazias
                continue

            try:
                response = chat_session.send_message(user_input)
                print(Style.BRIGHT + Fore.BLUE + f"\nGemini: {response.text} \n")
            except Exception as e:
                print(f"Erro durante o chat: {e}")
                # Poderia tentar reiniciar o chat ou apenas sair
                break
    else:
        print("Não foi possível iniciar a sessão de chat com o Gemini.")

    print("\nAplicação finalizada.")

if __name__ == "__main__":
    run_application()