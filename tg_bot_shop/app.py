import asyncio

from aiogram import Bot, types, Dispatcher
from aiogram.filters import CommandStart

bot = Bot(token='7223968806:AAFlYDE4Vys51z5LRlltDkKz2phjv-Mu3d8')

dp = Dispatcher()


@dp.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.answer('Start')


@dp.message()
async def echo(message: types.Message):
    text = message.text
    if text in ['Привет', 'привет', 'hi', 'hello']:
        await message.answer('И тебе привет')
    elif text in ['Пока', 'пока', 'пакеда', 'До свидания']:
        await message.answer('И тебе пока')
    else:
        await message.answer(message.text)


async def main():
    await dp.start_polling(bot)


asyncio.run(main())
