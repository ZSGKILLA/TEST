from telegram.ext import Updater, MessageHandler, Filters
import os

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

def handle_message(update, context):
    text = update.message.text.lower()

    if "gm" in text:
        update.message.reply_text("gm fren 🫡")
    elif "rug" in text:
        update.message.reply_text("⚠️ Rug alert! SPAT deployed.")
    elif "wen moon" in text:
        update.message.reply_text("🌕 When SPAT flips enough rugs, we moon.")
    elif "spat" in text:
        update.message.reply_text("🧽 Spat army on duty. We flip rugs, not hopes.")
    elif "flip me" in text:
        update.message.reply_text("🥞 You’ve been flipped by the SPAT.")
    elif "join" in text:
        update.message.reply_text("👋 Welcome! You’ve joined the SPAT Army. Flip rugs. Fry FUD. HODL strong.")

updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher
dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

print("🥄 SPATBot is FLIPPING...")
updater.start_polling()
updater.idle()
