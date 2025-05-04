import logging
import random
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import Message
from aiogram.filters import CommandStart
from aiogram import F
import os

TOKEN = "7951137634:AAHA94m5HZ4RhW0CjkNw5lGgv72e3Ur26R8"  # Твой токен

logging.basicConfig(level=logging.INFO)

# Создание бота и диспетчера
bot = Bot(token=TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher(storage=MemoryStorage())

# Удаление вебхука (если он установлен)
async def remove_webhook():
    await bot.delete_webhook()
    print("Webhook удален")

# Реакция на "чек"
@dp.message(F.text.lower() == "чек", F.chat.type.in_({"group", "supergroup"}))
async def handle_check(message: Message):
    await message.answer("Сасу")

# Реакция на "как сосал ...", начало текста
@dp.message(F.text.lower().startswith("как сосал"), F.chat.type.in_({"group", "supergroup"}))
async def handle_sosal(message: Message):
    phrases = [
        "сосал хорошо", "сосал вверх", "сосал ниже", "сосал мягче", "сосал глубже",
        "сосал точно", "сосал вовремя", "сосал так", "сосал наглухо", "сосал нормально",
        "сосал прямо", "сосал стильно", "сосал свежо", "сосал ближе", "сосал нежно",
        "сосал тонко", "сосал гладко", "сосал бодро", "сосал спешно", "сосал весело",
        "сосал смело", "сосал скрыто", "сосал мягонько", "сосал бодрячком", "сосал коротко",
        "сосал тягуче", "сосал ритмично", "сосал ясно", "сосал плотненько", "сосал бодренько",
        "сосал не медленно", "сосал бест", "сосал точно так", "сосал круто", "сосал метко",
        "сосал не слабо", "сосал потише", "сосал поглубже", "сосал сильнее", "сосал телесно",
        "сосал культурно", "сосал плотненько", "сосал натурально", "сосал химически", 
        "сосал нежданно", "сосал разом", "сосал складно", "сосал легко", "сосал в разнос",
        "сосал слаженно", "сосал ритм", "сосал тема", "сосал стиль", "сосал добро", 
        "сосал ровно", "сосал подряд", "сосал четко", "сосал жестко", "сосал балдежно",
        "сосал завидно", "сосал полегче"
    ]
    phrase = random.choice(phrases)
    await message.answer(f"{message.from_user.mention_html()} {phrase}")

# Запуск
async def main():
    await remove_webhook()  # Удаляем вебхук, если он был
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
