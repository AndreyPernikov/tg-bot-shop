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
    await message.answer(message.text)  # Упомянуть пользователя
    await message.reply(message.text)


async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


asyncio.run(main())
