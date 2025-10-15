from aiogram import Router, F
from aiogram.types import Message,FSInputFile
from aiogram.fsm.state import State ,StatesGroup
from aiogram.fsm.context import FSMContext
from search_func import DATA, get_page, search_title
import os
from images_bot import MENU_IMAGE , SEARCH_IMAGE
from details import *
from database import *
from search_func import *
from environs import Env
env = Env()
env.read_env()  

user_router = Router()
#BU CONNTACT BUUTON FUNCTIONIGA JAVOB BERADI NO RETURN
@user_router.message(F.text == "📞 Contact")
async def contact_handler(message:Message):
    await message.answer(CONNACT_US_BT,reply_markup=back_kb)


#BACK BUTTON FUNCTION
@user_router.message(F.text == "↩️ Back")
async def back_menu_handler(message:Message):
    
    await message.answer_photo(
    photo=MENU_IMAGE,
    caption=MENU_TEXT,
    reply_markup=menu_kb
)


#BOOK FEILD
@user_router.message(F.text == "📚 Books")
async def contact_handler(message:Message):
    await message.answer(MENU_TEXT,reply_markup=books_kb)


#SEARCH FEILD



#class for saving message text and what type is it title author genre like this
class Search(StatesGroup):
    title = State()
    author = State()
    genre = State()



#the function of the button SEARCH 
@user_router.message(F.text == "🔎 Search")
async def contact_handler(message: Message):
    await message.answer("Qidiruv turini tanlang:", reply_markup=search_kb)


#START OF SEARCH PROGRESS!!!
#the start search on title including State , setting state.text
@user_router.message(F.text == "🔎 Search by Title")
async def search_books_by_title(message: Message, state: FSMContext):
    await message.answer("Iltimos, kitob nomini kiriting:")
    #setting
    await state.set_state(Search.title)


#savine to state.title , with checking and giving result
@user_router.message(Search.title)
async def search_books_by_title_input(message: Message, state: FSMContext):
    title = message.text.strip()

    books = find_by_column(title=title)#bu query title genre author buyicha malumot qidiradi uni BIZGA LIST QILIB ICHIDA NOMLARI BULIB KELADI 


    if not books:#FIND BY COLUMN CANT FIND BOOK
        await message.answer("❌ Hech qanday natija topilmadi.")
        await state.clear()
        return

    DATA.clear()#IF DATA HAD DATA CLEAR ERASE IT
    DATA.extend(books)#ADDING BOOKS TO DATA 
    page = 1
    
    items = get_page(page)
    text = "\n".join([f"{i+1}. {item}" for i, item in enumerate(items)])
    markup = search_title(book_id=1, count=page)

    await message.answer(f"🔎 Natijalar ({len(books)} ta topildi):\n\n{text}", reply_markup=markup)
    await state.clear()
@user_router.message(F.text == "🔎 Search by Author")
async def search_books_by_author(message: Message, state: FSMContext):
    await message.answer("Iltimos, muallif nomini kiriting:")
    await state.set_state(Search.author)

@user_router.message(Search.author)
async def search_books_by_author_input(message: Message, state: FSMContext):
    author = message.text.strip()
    books = find_by_column(author=author)

    if not books:
        await message.answer("❌ Hech qanday natija topilmadi.")
        await state.clear()
        return

    DATA.clear()
    DATA.extend(books)

    page = 1 
    items = get_page(page)
    text = "\n\n".join([f"👤 {item}" for item in items])
    markup = search_title(book_id=1, count=page)

    await message.answer(f"🔎 Muallif bo‘yicha natijalar ({len(books)} ta topildi):\n\n{text}", reply_markup=markup)
    await state.clear()


@user_router.message(F.text == "🔎 Search by Genre")
async def search_books_by_genre(message: Message, state: FSMContext):
    await message.answer("Iltimos, janr nomini kiriting:")
    await state.set_state(Search.genre)


@user_router.message(Search.genre)
async def search_books_by_genre_input(message: Message, state: FSMContext):
    genre = message.text.strip()
    books = find_by_column(genre=genre)

    if not books:
        await message.answer("❌ Hech qanday natija topilmadi.")
        await state.clear()
        return

    DATA.clear()
    DATA.extend(books)

    page = 1
    items = get_page(page)
    text = "\n\n".join([f"🎭 {item}" for item in items])
    markup = search_title(book_id=1, count=page)

    await message.answer(f"🔎 Janr bo‘yicha natijalar ({len(books)} ta topildi):\n\n{text}", reply_markup=markup)
    await state.clear()
#Profile Uchun Kersak
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
    await message.answer(ORDERS_TEXT,reply_markup=order_kb)
    
@user_router.message(F.text == "🛒 Ordered Books")
async def contact_handler(message:Message):
    await message.answer(CONNACT_US_BT,reply_markup=order_inb)






