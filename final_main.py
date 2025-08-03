import asyncio
from datetime import datetime
from pytz import timezone
import telegram
from market_fetcher import coletar_todos_os_dados, gerar_mensagem_mercado

# === CONFIGURAÇÕES DO TELEGRAM ===
TELEGRAM_TOKEN = "Digitar o token"
TELEGRAM_CHAT_ID = "Digitar o chatID"
bot = telegram.Bot(token=TELEGRAM_TOKEN)

# === HORÁRIOS DE ENVIO (horário de Brasília) ===
HORARIOS_ENVIO = ["06:00", "08:00", "10:00", "10:40", "13:00", "17:00", "21:00"]

# Retorna o horário atual de Brasília (formato HH:MM)
def horario_brasilia():
    tz = timezone("America/Sao_Paulo")
    return datetime.now(tz).strftime("%H:%M")

# Loop principal que roda a cada 30 segundos
enviados_hoje = set()
async def iniciar_envios():
    print("\n📡 Bot de Panorama de Mercado iniciado...")
    while True:
        hora_atual = horario_brasilia()

        if hora_atual in HORARIOS_ENVIO and hora_atual not in enviados_hoje:
            print(f"[ {hora_atual} ] Enviando panorama...")
            dados = coletar_todos_os_dados()
            mensagem = gerar_mensagem_mercado(dados)
            await bot.send_message(chat_id=TELEGRAM_CHAT_ID, text=mensagem, parse_mode=telegram.constants.ParseMode.MARKDOWN)
            enviados_hoje.add(hora_atual)

        # Resetar a lista à meia-noite
        if hora_atual == "00:00":
            enviados_hoje.clear()

        await asyncio.sleep(30)  # Aguarda 30 segundos antes de verificar de novo

# Execução principal
if __name__ == '__main__':
    asyncio.run(iniciar_envios())


