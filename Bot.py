import asyncio
from telegram import Bot

BOT_TOKEN = '8049818427:AAFmKLhGNUTI7qxNvwlq8eBNG7JWrqy9GIc'
CHAT_ID = '-1002157107652'

bot = Bot(token=BOT_TOKEN)

async def main():
    await bot.send_message(chat_id=CHAT_ID, text="ربات با موفقیت اجرا شد.")

asyncio.run(main())
