from .search_ikb import * 
from aiogram import Router ,F
from aiogram.types import CallbackQuery,Message


sch = Router()

@sch.callback_query(F.data.startwith("save"))
async def call_backdata_search_books(call:CallbackQuery):
    await call.message(text="salom")