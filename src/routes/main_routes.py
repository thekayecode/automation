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
# Make sure to add the TELEGRAM_BOT_TOKEN in your Render environment variables (without quotes)
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

# Make sure to start the polling or webhook for Telegram to receive updates
# If you're using polling (during local dev):
# telegram_app.run_polling()

# If you're using webhooks in production, you can skip the polling step and rely on webhooks instead.
