import os
from fastapi import APIRouter, Request
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes,
)

router = APIRouter()

# Load your bot token from environment variables
TELEGRAM_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

# Ensure the token is provided
if TELEGRAM_TOKEN is None:
    raise ValueError("TELEGRAM_BOT_TOKEN not found in environment variables!")

# Build the Telegram app
telegram_app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

# Webhook endpoint for Telegram
@router.post("/webhook")
async def telegram_webhook(req: Request):
    data = await req.json()
    update = Update.de_json(data, telegram_app.bot)
    await telegram_app.process_update(update)
    return {"status": "ok"}

# Bot command: /start
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 Hey! I'm alive and running on Render. Let’s automate some content!")

# Register the /start handler
telegram_app.add_handler(CommandHandler("start", start_command))

# Comment this out in production, leave it for local dev:
# telegram_app.run_polling()

