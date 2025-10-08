from aiogram import Router, F
from aiogram.types import Message,FSInputFile
from aiogram.fsm.state import State ,StatesGroup
from aiogram.fsm.context import FSMContext
from details import *
from database import *
from search_func import *
from environs import Env
env = Env()
env.read_env()  

user_router = Router()
#Contact uchun kerak 
@user_router.message(F.text == "📞 Contact")
async def contact_handler(message:Message):
    await message.answer(CONNACT_US_BT,reply_markup=back_kb)
#Back da endi 
@user_router.message(F.text == "↩️ Back")
async def contact_handler(message:Message):
    path = "images/menu_image.jpg"

    await message.answer_photo(photo = FSInputFile(path=path),caption=MENU_TEXT,reply_markup=menu_kb)
    
#book uchun kerak
@user_router.message(F.text == "📚 Books")
async def contact_handler(message:Message):
    await message.answer(CONNACT_US_BT,reply_markup=books_kb)
#search maydoni
class SearchBook(StatesGroup):
    search_type = State()
    text = State()

    
@user_router.message(F.text == "🔎 Search")
async def contact_handler(message:Message):
    await message.answer(CONNACT_US_BT,reply_markup=search_kb)
@user_router.message(F.text=="🔎 Search by Titlte")
async def search_books_by_title(message:Message):  
    await message.answer(text="Iltimos kitob nomini kiriting: ")
@user_router.message(F.text=="🔎 Search by Author")
async def search_books_by_author(message:Message):
    await message.answer(text="Iltimos muallif nomini kiriting: ")
@user_router.message(F.text=="🔎 Search by Genre")
async def search_books_by_genre(message:Message):
    await message.answer(text="Iltimos genre nomini kiriting: ")


#Profile Uchun Kerak
@user_router.message(F.text == "👤 Profile")
async def contact_handler(message:Message):
    await message.answer(PROFILE,reply_markup=profile_kb)
#username Almashtirish
@user_router.message(F.text == "✏️ Change username")
async def contact_handler(message:Message):
    await message.answer(USERNAME_CHANGE,reply_markup=profile_kb)

#About Me Ishlaydi 
@user_router.message(F.text == "👤 About Me")
async def contact_handler(message:Message):
    for i in get_user_data(message.from_user.id):
        result = {
            "name":i[0],
            "phone":i[1],
            "username":i[2],
            "location":i[3]

        }
    
    text = (
    f"👤 Ism: {result['name']}\n"
    f"📞 Nomer: {result['phone']}\n"
    f"🔗 Username: @{result['username']}\n"
    f"📍 Joylashuv: {result['location']}"
)


    await message.answer(text,reply_markup=profile_kb)


#Order Uchun Kerak 
@user_router.message(F.text == "📝 Order")
async def contact_handler(message:Message):
    await message.answer(CONNACT_US_BT,reply_markup=order_kb)
    
@user_router.message(F.text == "🛒 Ordered Books")
async def contact_handler(message:Message):
    await message.answer(CONNACT_US_BT,reply_markup=order_inb)






