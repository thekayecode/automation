import os
from dotenv import load_dotenv  # To load environment variables from a .env file
from telegram import Update  # For handling updates from Telegram
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes  # For creating the bot app and command handlers

# Load environment variables from the .env file
load_dotenv()

# Get the bot token from environment variables
BOT_TOKEN = os.getenv("BOT_TOKEN")

# If the bot token is not found in the environment, raise an error
if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN is not set in environment variables or the .env file.")

# Create the Telegram bot app using the bot token
app = ApplicationBuilder().token(BOT_TOKEN).build()

# Define the handler for the /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! I'm alive.")  # Respond with a message when the /start command is issued

# Add the handler for the /start command
app.add_handler(CommandHandler("start", start))

# Start polling to listen for messages and commands
app.run_polling()
