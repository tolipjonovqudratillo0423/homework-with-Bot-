from environs import Env 
from aiogram import Bot, Dispatcher
from aiogram .types import Message,ReplyKeyboardRemove
from logging import basicConfig,INFO
from handler import user_router,register_router
import asyncio
env = Env()
env.read_env()
dp = Dispatcher()







async def main():
    bot = Bot(token=str(env('TOKEN')))
    try:
        basicConfig(level=INFO)
        dp.include_router(register_router)
        dp.include_router(user_router)
        await dp.start_polling(bot)
    finally:
        await bot.session.close()
if __name__ == '__main__':
    asyncio.run(main())

    