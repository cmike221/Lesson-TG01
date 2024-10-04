import asyncio
import requests
from aiogram import Bot, Dispatcher, F, types
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from config import TOKEN, OPENWEATHERMAP_API_KEY

import random
WEATHER_API_KEY = OPENWEATHERMAP_API_KEY

bot = Bot(token=TOKEN)
dp = Dispatcher()


@dp.message(Command('start'))
async def start(message: Message):
    await message.answer('Привет! Я бот, выдаю прогноз погоды на завтра. Введи название города:')


@dp.message(Command('help'))
async def help(message: Message):
    await message.answer('Этот бот умеет выполнять команды: \n /start \n /help')


@dp.message()
async def get_weather(message: types.Message):
    city = message.text
    await message.answer(F"Запрос погоды в {city}")
    weather_data = fetch_weather(city)
    # await message.answer("Обработка ...")

    if weather_data:
        await message.answer(weather_data)
    else:
        await message.answer("Не удалось получить данные о погоде. Проверьте название города и попробуйте снова.")


def fetch_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}&units=metric"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        tomorrow_weather = f"Погода в городе {city} на завтра:\n" \
                           f"Температура: {data['main']['temp']}°C\n" \
                           f"Описание: {data['weather'][0]['description']}\n" \
                           f"Влажность: {data['main']['humidity']}%\n" \
                           f"Скорость ветра: {data['wind']['speed']} м/с"
        return tomorrow_weather
    else:
        return None


async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
