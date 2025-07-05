from fastapi import Request
from telegram import Update, Bot
from telegram.ext import Dispatcher, CommandHandler
import os

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
bot = Bot(token=TOKEN)

@router.post("/webhook")
async def telegram_webhook(req: Request):
    data = await req.json()
    update = Update.de_json(data, bot)
    dp = Dispatcher(bot, None, workers=0)
    
    def start(update, context):
        update.message.reply_text("Hello, this is your bot!")

    dp.add_handler(CommandHandler("start", start))
    dp.process_update(update)
    return {"ok": True}
