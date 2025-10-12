from aiogram import Bot , Router, F
from aiogram.types import Message, ReplyKeyboardRemove,FSInputFile
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.filters import CommandStart
from environs import Env
from details import *
from images_bot import *
from database import *
import os
env = Env()
env.read_env()

register_router  = Router()
class Reg_point(StatesGroup):
    chat_id = State()
    name = State()
    phone = State()
    username = State()
    location = State()
    


@register_router.message(CommandStart())
async def command_start(message: Message ):
    
    await message.answer(REG_text,reply_markup=register_kb)


@register_router .message(F.text == "📝 Register")

async def register(message:Message, state: FSMContext):
    
    
    if check_user(message.from_user.id):
        await message.answer_photo(
    photo=MENU_IMAGE,
    caption=MENU_TEXT,
    reply_markup=menu_kb
)
    else:
        await state.set_state(Reg_point.name)
        await message.answer(GET_NAME_TEXT)
        await state.update_data(chat_id=message.from_user.id)


    
@register_router.message(Reg_point.name)
async def command_name(message: Message, state: FSMContext):
    
    if validate_name(message.text):
        await state.update_data(name=message.text)
        await message.answer(GET_PHONE_TEXT, reply_markup=share_phone_kb)
        await state.set_state(Reg_point.phone)
    else:
        await message.answer("Please Enter Corrected Version Of Your NAME !!!")

        
@register_router.message(Reg_point.phone)
async def command_phone(message: Message, state: FSMContext):
    if message.contact:
            phone = message.contact.phone_number
    else:
        if validate_phone(message.text):
            phone = message.text
             
        else:
            await message.answer("Please Enter Corrected Version Of Your Phone Number !!!")
            return
    await state.update_data(phone=phone)
    await state.set_state(Reg_point.username)
    await message.answer(
        "👍 Phone number saved!\n\n"
        "Now I will automatically use your Telegram username.\n"
        "➡️ Press any key or just continue...",
        reply_markup=continue_button)    
@register_router.message(Reg_point.username)
async def command_username(message: Message, state: FSMContext):
    try:
        username = message.from_user.username
    except:
        pass

    await state.update_data(username=username)
    await state.set_state(Reg_point.location)
    await message.answer(GET_LOCATION_TEXT, reply_markup=location_share_kb)

        


@register_router .message(Reg_point.location)
async def command_location(message: Message, state: FSMContext):
    if message.location is not None:
        location = f'{message.location.latitude}, {message.location.longitude}'
    else:
        location = message.text
    await state.update_data(location=location)
    data = await state.get_data()
    
    
    await message.answer(
            f"✅ *Registration completed!*\n\n"
            f"🆔 Chat ID: `{data['chat_id']}`\n"
            f"👤 Name: {data['name']}\n"
            f"📱 Phone: {data['phone']}\n"
            f"📛 Username: @{data['username']}\n"
            f"📍 Location: {data['location']}",
            parse_mode="Markdown",
            reply_markup=ReplyKeyboardRemove()
            
        )
    await message.answer(MENU_TEXT, reply_markup=menu_kb)

        
    get_connect()
    create_important_table()
    insert_query(data['chat_id'],data['name'],data['phone'],data['username'],data['location'])

    await state.clear()







    
