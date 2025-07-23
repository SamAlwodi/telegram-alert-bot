from fastapi import FastAPI
from telegram import Bot

app = FastAPI()

BOT_TOKEN = "8079495838:AAGQxEX7soXiXo0SXcxTBdSH_Sx4D1kdcOw"
CHAT_ID = "@AlwodiTradeBot"  # or use your numeric chat ID
bot = Bot(token=BOT_TOKEN)

@app.get("/")
def read_root():
    return {"status": "Telegram bot is running!"}

@app.get("/send")
def send_signal(
    pair: str = "XAUUSD",
    entry: float = 0.0,
    sl: float = 0.0,
    tp: float = 0.0,
    reason: str = "OBV + CCI confirmation",
):
    message = f"""
📢 TRADE SIGNAL – {pair}
📍 Entry: {entry}
🎯 TP: {tp} | ⛔ SL: {sl}
📊 Reason: {reason}
🕐 Sent via Render bot
"""
    bot.send_message(chat_id=CHAT_ID, text=message)
    return {"status": "Signal sent"}
