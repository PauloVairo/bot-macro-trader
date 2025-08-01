
# main.py
# BOT DE NOTÍCIAS E EVENTOS MACROECONÔMICOS PARA TELEGRAM
# Autor: Paulo + GPT
# Executa dois fluxos principais: Agenda de eventos macro e notícias filtradas por palavras-chave
# Notificações são enviadas via Telegram

import requests
import time
import datetime
import pytz
from keep_alive import keep_alive

# ==== CONFIGURAÇÕES ====
TELEGRAM_TOKEN = "SEU_TOKEN_AQUI"
CHAT_ID = "SEU_CHAT_ID_AQUI"

# PALAVRAS-CHAVE POR CATEGORIA
KEYWORDS = {
    "politica_monetaria": [
        "fed", "fomc", "juros", "taxa de juros", "hawkish", "dovish",
        "powell", "bcb", "selic", "copom", "trump", "lula", "christine lagarde", "xi jinping"
    ],
    "inflacao_economia": [
        "inflação", "cpi", "pce", "ipca", "igp", "preços", "custos", "núcleos", "ppi"
    ],
    "atividade_economica": [
        "pib", "gdp", "produção", "consumo", "atividade", "manufatura", "ism", "pmi"
    ],
    "emprego": [
        "payrolls", "desemprego", "jobless", "empregos", "earnings", "salários", "renda"
    ],
    "risco": [
        "guerra", "ataque", "default", "crise", "instabilidade", "greve", "falência", "rebaixamento", "colapso"
    ],
    "liquidez": [
        "qt", "qe", "balanço do fed", "stress bancário", "liquidez", "emergência"
    ],
    "tecnologia": [
        "apple", "microsoft", "google", "meta", "big tech", "resultados", "guidance", "amazon"
    ],
    "bancos": [
        "bancos", "crédito", "jp morgan", "goldman", "bradesco", "itau", "caixa"
    ]
}

def enviar_telegram(mensagem):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": mensagem, "parse_mode": "Markdown"}
    requests.post(url, data=data)

# SIMULANDO FLUXO DE FUNCIONAMENTO (simplificado para exemplo)
def rotina_bot():
    while True:
        agora = datetime.datetime.now(pytz.timezone('America/Sao_Paulo'))
        hora = agora.strftime("%H:%M")
        print(f"Executando bot... {hora}")

        # Exemplo simulado de aviso às 23h
        if hora == "23:00":
            enviar_telegram("📅 *Agenda de Eventos Macroeconômicos* para amanhã será enviada.")
            # Aqui entraria a lógica para buscar e filtrar os eventos do dia seguinte

        # Simulação: checar notícia nova (RSS) e bater com palavras-chave
        # Aqui entraria lógica de RSS com filtragem por KEYWORDS
        
        time.sleep(60)

# Iniciar keep_alive (caso esteja rodando no Replit)
keep_alive()

# Iniciar rotina principal
rotina_bot()
