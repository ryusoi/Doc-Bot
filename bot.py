import os
from telegram.ext import ApplicationBuilder, CommandHandler
import openai

TELEGRAM_BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
openai.api_key = OPENAI_API_KEY

async def start(update, context):
    await update.message.reply_text("Hey! I'm alive on Fly.io!")

app = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.run_polling()
