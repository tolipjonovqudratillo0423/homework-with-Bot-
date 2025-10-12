import os 
from aiogram import Bot, Dispatcher
from aiogram .types import Message,ReplyKeyboardRemove
from logging import basicConfig,INFO
from handler import user_router,register_router ,search_router
import asyncio
TOKEN = os.getenv("TOKEN")
dp = Dispatcher()


async def main():
    bot = Bot(token=TOKEN)
    try:
        basicConfig(level=INFO)
        dp.include_router(register_router)
        dp.include_router(user_router)
        dp.include_router(search_router)
        await dp.start_polling(bot)
    finally:
        await bot.session.close()
if __name__ == '__main__':
    asyncio.run(main())

    