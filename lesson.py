import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from config import TOKEN

import random

bot = Bot(token=TOKEN)
dp = Dispatcher()


@dp.message(Command('photo'))
async def photo(message: Message):
    list = ['https://telegra.ph/file/336d9fc28d60a72bd3694.jpg', 'https://i.pinimg.com/736x/ba/53/7b/ba537bfc9d0d55235bd9c1ddf978f1cb.jpg', 'https://botsila.ru/wp-content/uploads/2022/06/Screenshot_643-1.png']
    rand_photo = random.choice(list)
    await message.answer_photo(photo=rand_photo, caption="Это супер картинка")


@dp.message(F.photo)
async def react_photo(message: Message):
    list = ['Ого, какая фотка!', 'что это такое?', 'Не отправляй мне больше это!']
    rand_answ = random.choice(list)
    await message.answer(rand_answ)


@dp.message(F.text == "Что такое ИИ?")
async def aitext(message: Message):
    await message.answer('ИИ - это свойство интеллектуальных систем ...')


@dp.message(Command('help'))
async def help(message: Message):
    await message.answer('Этот бот умеет выполнять команды: \n /start \n /help')


@dp.message(CommandStart)
async def start(message: Message):
    await message.answer('Привет! Я бот!')


async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
