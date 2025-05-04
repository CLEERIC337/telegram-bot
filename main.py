import random
from aiogram import Bot, Dispatcher, types
from aiogram.types import ParseMode
import logging

API_TOKEN = '7951137634:AAHA94m5HZ4RhW0CjkNw5lGgv72e3Ur26R8'

# Включаем логирование, чтобы отслеживать, что происходит с ботом
logging.basicConfig(level=logging.INFO)

# Создаем объект бота и диспетчера
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# Список фраз для команды "как сосал"
phrases = [
    "сосал хорошо", "сосал вверх", "сосал ниже", "сосал мягче", "сосал глубже", 
    "сосал точно", "сосал вовремя", "сосал так", "сосал наглухо", "сосал норм", 
    "сосал прямо", "сосал стильно", "сосал свежо", "сосал ближе", "сосал нежно", 
    "сосал тонко", "сосал гладко", "сосал бодро", "сосал спешно", "сосал весело", 
    "сосал смело", "сосал скрыто", "сосал мягонько", "сосал бодрячком", "сосал кратно", 
    "сосал тягуче", "сосал ритмично", "сосалнятно", "сосал плотненько", "сосал бодренько", 
    "сосал не медленно", "сосал бест", "сосал точно так", "сосал круто", "сосал метко", 
    "сосал не слабо", "сосал потише", "сосал поглубже", "сосал сильнее", "сосал телесно", 
    "сосал культурно", "сосал плотненько", "сосал натурально", "сосал химически", 
    "сосал нежданно", "сосал разом", "сосал складно", "сосал ихимико", "сосал разнос", 
    "сосал слаженно", "сосал ритм", "сосал тема", "сосал стайл", "сосал добро", 
    "сосал ровно", "сосал подряд", "сосал четко", "сосал жестко", "сосал балдежно", 
    "сосал завидно", "сосал полегче"
]

# Обработчик команды "чек"
@dp.message_handler(lambda message: message.text.lower() == "чек" and len(message.text.split()) == 1)
async def handle_check(message: types.Message):
    await message.answer("Сасу")

# Обработчик команды "как сосал"
@dp.message_handler(lambda message: message.text.lower() == "как сосал" and len(message.text.split()) == 2)
async def handle_sosal(message: types.Message):
    # Случайным образом выбираем фразу из списка
    random_phrase = random.choice(phrases)
    # Отправляем ответ
    await message.answer(f"{message.from_user.get_mention()} сегодня ты {random_phrase}!")

# Запускаем бота
if __name__ == '__main__':
    from aiogram import executor
    executor.start_polling(dp, skip_updates=True)
