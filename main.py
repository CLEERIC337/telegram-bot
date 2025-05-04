from aiogram import Bot, Dispatcher, types
import logging
import random
from aiohttp import web
from aiogram.utils.executor import start_webhook

API_TOKEN = '7951137634:AAHA94m5HZ4RhW0CjkNw5lGgv72e3Ur26R8'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# Define webhook settings
WEBHOOK_HOST = 'https://telegram-bot-9ze3.onrender.com'  # Замените на ваш URL с Render
WEBHOOK_PATH = '/webhook'
WEBHOOK_URL = f"{WEBHOOK_HOST}{WEBHOOK_PATH}"

# Set webhook
async def on_start_webhook(app):
    await bot.set_webhook(WEBHOOK_URL)

# Handle the 'чек' command
@dp.message_handler(lambda message: message.text.lower() == "чек" and len(message.text.split()) == 1)
async def handle_check(message: types.Message):
    await message.answer("Сасу")

# Handle the 'как сосал' command
@dp.message_handler(lambda message: message.text.lower() == "как сосал" and len(message.text.split()) == 2)
async def handle_sosal(message: types.Message):
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
    random_phrase = random.choice(phrases)
    await message.answer(f"{message.from_user.get_mention()} сегодня ты {random_phrase}!")

# Create aiohttp app and run it
app = web.Application()
app.on_startup.append(on_start_webhook)

# Run webhook using aiohttp app and aiogram dispatcher
if __name__ == '__main__':
    start_webhook(
        dispatcher=dp,
        webhook_path=WEBHOOK_PATH,
        app=app,
        host='0.0.0.0',
        port=8080  # Render автоматически определяет порт
    )
