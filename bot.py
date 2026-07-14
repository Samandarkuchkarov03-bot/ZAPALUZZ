import asyncio
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message
TOKEN = "8908557730:AAHmQ5T1xgexNHBABAvkBqL6xERhaEGwM3A"

bot = Bot(token=TOKEN)
dp = Dispatcher()
@dp.message(CommandStart())
async def start(message: Message):
    await message.answer("🎬 Assalomu alaykum!\n\nKino kodini yuboring.")
async def main():
        await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
