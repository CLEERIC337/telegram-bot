import logging
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

API_TOKEN = '7951137634:AAHA94m5HZ4RhW0CjkNw5lGgv72e3Ur26R8'  # твой токен

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(lambda message: message.text and message.text.lower() == "чек")
async def send_check(message: types.Message):
    await message.reply("Сасу")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
