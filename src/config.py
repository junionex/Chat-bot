# src/config.py
import os
from dotenv import load_dotenv

# Carrega as variáveis do arquivo .env para o ambiente
load_dotenv()

# Obtém a chave API do ambiente
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

if not GOOGLE_API_KEY:
    print("Atenção: A variável de ambiente GOOGLE_API_KEY não foi definida.")
    # Você pode optar por levantar uma exceção aqui se a chave for crucial
    # raise ValueError("GOOGLE_API_KEY não encontrada. Verifique seu arquivo .env")