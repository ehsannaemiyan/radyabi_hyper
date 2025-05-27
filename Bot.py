import os
from telegram import Bot

bot_token = os.getenv("BOT_TOKEN")
chat_id = os.getenv("CHAT_ID")

bot = Bot(token=bot_token)
bot.send_message(chat_id=chat_id, text="ربات با موفقیت اجرا شد.")
