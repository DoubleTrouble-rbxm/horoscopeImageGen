import asyncio
import logging
import os
import sys
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, html
from aiogram.client import bot
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message, FSInputFile
import image_gen

load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")
allowedIds = [1281277432, 1247358174, 806384140, 7730827014]
dp = Dispatcher()

@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    if message.from_user.id in allowedIds:
        await message.answer(f"Привет, {html.bold(message.from_user.full_name)}! Пиши текст")
    else:
        await message.answer(f"Гуляй вася")

@dp.message()
async def msgHandler(message: Message) -> None:
    if message.from_user.id in allowedIds:
        image_gen.generateImage(message.text)
        img = FSInputFile("result.png")
        await message.bot.send_photo(message.chat.id, img)
        print(f"Сгенерировано изображение с текстом '{message.text}'")
    else:
        await message.answer(f"Гуляй вася")


async def main() -> None:
    # Initialize Bot instance with default bot properties which will be passed to all API calls
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    # And the run events dispatching
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())