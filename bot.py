# bot.py
import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from dotenv import load_dotenv

# Charger les variables d'environnement depuis le fichier .env
load_dotenv()
TOKEN = os.getenv("TELEGRAM_TOKEN")

# Fonction appelée quand on tape /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("\u2705 Bot activ\u00e9 ! Tu recevras bient\u00f4t tes alertes crypto.")

# Initialisation et lancement du bot
if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    print("Bot démarre...")
    app.run_polling()
