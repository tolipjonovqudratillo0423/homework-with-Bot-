from aiogram import Bot , Router, F
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.filters import CommandStart
from environs import Env
from pops import REG_text,register_kb,share_phone_kb,location_share_kb
from database import get_connect, create_important_table, insert_query
env = Env()
env.read_env()

user_router = Router()
class Reg_point(StatesGroup):
    chat_id = State()
    name = State()
    phone = State()
    username = State()
    location = State()
    


@user_router.message(CommandStart())
async def start(message: Message ):
    
    await message.answer(REG_text,reply_markup=register_kb)


@user_router.message(F.text == "Register")
async def register(message:Message, state: FSMContext):
    await state.set_state(Reg_point.name)
    await message.answer("Enter your name")
    await state.update_data(chat_id=message.from_user.id)


    
@user_router.message(Reg_point.name)
async def command_name(message: Message, state: FSMContext):
    await message.answer("Please share your phone number", reply_markup=share_phone_kb)
    await state.update_data(name=message.text)
    await state.set_state(Reg_point.phone)

        
@user_router.message(Reg_point.phone)
async def command_phone(message: Message, state: FSMContext):
    if message.contact:
        phone = message.contact.phone_number
    else:
        phone = message.text
    await state.update_data(phone=phone)
    await state.set_state(Reg_point.username)
    await message.answer("Enter your username", reply_markup=ReplyKeyboardRemove())




@user_router.message(Reg_point.username)
async def command_username(message: Message, state: FSMContext):
    try:
        username = message.from_user.username
    except:
        username = message.text

    await state.update_data(username=username)
    await state.set_state(Reg_point.location)
    await message.answer("Enter your location", reply_markup=location_share_kb)



@user_router.message(Reg_point.location)
async def command_location(message: Message, state: FSMContext):
    if message.location is not None:
        location = (message.location.latitude, message.location.longitude)
    else:
        location = message.text
    await state.update_data(location=location)
    data = await state.get_data()
    await message.answer(f"Registration completed!\n\n"
                         f"Chat ID: {data['chat_id']}\n"
                         f"Name: {data['name']}\n"
                         f"Phone: {data['phone']}\n"
                         f"Username: {data['username']}\n"

                         f"Location: {data['location']}\n", reply_markup=ReplyKeyboardRemove())
    get_connect()
    create_important_table()
    insert_query(data['chat_id'],data['name'],data['phone'],data['username'],data['location'])

    await state.clear()







    
