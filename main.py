from aiogram import Bot, Dispatcher, types
import logging
import random
from aiohttp import web
from aiogram.fsm.storage.memory import MemoryStorage

API_TOKEN = '7951137634:AAHA94m5HZ4RhW0CjkNw5lGgv72e3Ur26R8'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(storage=storage, bot=bot)

# Define webhook settings
WEBHOOK_HOST = 'https://telegram-bot-9ze3.onrender.com'  # Замените на ваш URL с Render
WEBHOOK_PATH = '/webhook'
WEBHOOK_URL = f"{WEBHOOK_HOST}{WEBHOOK_PATH}"

# Set webhook
async def on_start_webhook(app):
    await bot.set_webhook(WEBHOOK_URL)

# Handle the 'чек' command
async def handle_check(message: types.Message):
    if message.text.lower() == "чек" and len(message.text.split()) == 1:
        await message.answer("Сасу")

# Handle the 'как сосал' command
async def handle_sosal(message: types.Message):
    if message.text.lower() == "как сосал" and len(message.text.split()) == 2:
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

# Register handlers
dp.message.register(handle_check)
dp.message.register(handle_sosal)

# Create aiohttp app and run it
app = web.Application()
app.on_startup.append(on_start_webhook)

# Handle webhook
async def handle_webhook(request):
    json_obj = await request.json()
    update = types.Update(**json_obj)
    Dispatcher.set_current(dp)
    await dp.process_update(update)
    return web.Response()

app.router.add_post(WEBHOOK_PATH, handle_webhook)

# Run aiohttp app
if __name__ == '__main__':
    web.run_app(app, host='0.0.0.0', port=8080)
