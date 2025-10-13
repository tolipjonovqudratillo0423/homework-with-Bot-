from aiogram import Router, F, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton ,CallbackQuery
from aiogram.utils.keyboard import InlineKeyboardBuilder

search_router = Router()


DATA = [f"Book {i}" for i in range(1, 51)]
ITEMS_PER_PAGE = 5 


def search_title(book_id,count=1):
    
    search_by_title = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text='◀️ Back',callback_data=f"back_{book_id}_{count-1}"), InlineKeyboardButton(text=f"{count}",callback_data=f"number"),InlineKeyboardButton(text="Next ▶️",callback_data=f"next_{book_id}_{count+1}")],

            [InlineKeyboardButton(text="Cancel ❌",callback_data="cancel"),InlineKeyboardButton(text="Send 🚀",callback_data=f"send_{book_id}")]
        ]
    )
    return search_by_title

def get_page(page: int):
    start = (page - 1) * ITEMS_PER_PAGE
    end = start + ITEMS_PER_PAGE
    return DATA[start:end]

@search_router.message(F.text == "🔎 Search")
async def search_handler(message: types.Message):
    page = 1
    items = get_page(page)
    text = "\n\n".join([f"📘 {item}" for item in items])
    markup = search_title(book_id=1, count=page)
    markup2 = select_buttons(book_id=1, page=page)
    full_markup = InlineKeyboardMarkup(
        inline_keyboard=markup+ markup2
    )
    await message.answer(text, reply_markup=full_markup)
    


@search_router.callback_query(F.data.startswith("next_"))
async def next_page(callback: types.CallbackQuery):
    _, book_id, page = callback.data.split("_")
    page = int(page)
    items = get_page(page)
    if not items:
        await callback.answer("🚫 Bu oxirgi sahifa", show_alert=True)
        return

    text = "\n\n".join([f"📘 {item}" for item in items])
    markup = search_title(book_id, count=page)
    await callback.message.edit_text(text, reply_markup=markup)
    await callback.answer()



@search_router.callback_query(F.data.startswith("back_"))
async def back_page(callback: types.CallbackQuery):
    _, book_id, page = callback.data.split("_")
    page = int(page)
    if page < 1:
        await callback.answer("🚫 Bu birinchi sahifa", show_alert=True)
        return

    items = get_page(page)
    text = "\n\n".join([f"📘 {item}" for item in items])
    markup = search_title(book_id, count=page)
    await callback.message.edit_text(text, reply_markup=markup)
    await callback.answer()

#1,2,3,4,5 buttons
def select_buttons(book_id, page):
    rows = []
    buttons_per_row = 5  

    for i in range(1, 11):
        btn = InlineKeyboardButton(
            text=f"{i}",  
            callback_data=f"select_{book_id}_{page}_{i}"  
        )

        
        if (i - 1) % buttons_per_row == 0:
            rows.append([btn])
        else:
            rows[-1].append(btn)

    return InlineKeyboardMarkup(inline_keyboard=rows)
# @search_router.callback_query(F.data.startwith("select_"))
# async def send_books(call:CallbackQuery):
#     book_id = call.data
