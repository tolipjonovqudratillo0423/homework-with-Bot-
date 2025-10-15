from aiogram import Router, F, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton ,CallbackQuery
from aiogram.utils.keyboard import InlineKeyboardBuilder
#import i,portant modules 
search_router = Router()

#DATA IT'S JUST LIST FOR SAVING DATA
DATA = []
ITEMS_PER_PAGE = 10 #HOW MUCH BOOKS IN ONE PAGE

#THIS FUNC WORK FOR SHOWING A INLINE BUTTONS
def select_buttons(book_id, page):
    rows = []#it is collection of inline buttons
    buttons_per_row = 5

    for i in range(1, 11):#param for creating 
        btn = InlineKeyboardButton(
            text=f"{i}",#i is 1,2,3,4,5,6,7,8,9,10
            callback_data=f"select_{book_id}_{page}_{i}"#book_id and page is given in param but i is given in loop
        )
        if (i - 1) % buttons_per_row == 0:#there are checking i for dividing correctly to rows
            rows.append([btn])
        else:
            rows[-1].append(btn)

    return InlineKeyboardMarkup(inline_keyboard=rows)


def search_title(book_id,count=1):#back and next buttons
    
    search_by_title = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text='◀️ Back',callback_data=f"back_{book_id}_{count-1}"), InlineKeyboardButton(text=f"{count}",callback_data=f"number"),InlineKeyboardButton(text="Next ▶️",callback_data=f"next_{book_id}_{count+1}")],

            [InlineKeyboardButton(text="Cancel ❌",callback_data="cancel"),InlineKeyboardButton(text="Send 🚀",callback_data=f"send_{book_id}")]
        ]
    )
    return search_by_title

def get_page(page: int):# get page is for detecting start and end of find book
    start = (page - 1) * ITEMS_PER_PAGE
    end = start + ITEMS_PER_PAGE
    return DATA[start:end]


@search_router.message(F.text == "🔎 Search")
async def search_handler(message: types.Message):
    page = 1
    items = get_page(page)
    text = "\n".join([f"{i+1}. {item}" for i, item in enumerate(items)])
    markup = search_title(book_id=1, count=page)
    markup2 = select_buttons(book_id=1, page=page)
    full_markup = InlineKeyboardMarkup(
        inline_keyboard=markup2.inline_keyboard + markup.inline_keyboard
    )

    await message.answer(text, reply_markup=full_markup)


@search_router.callback_query(F.data.startswith("next_"))#callback for next
async def next_page(callback: types.CallbackQuery):
    _, book_id, page = callback.data.split("_") #dividing to three objects (next,book_id,page)
    page = int(page)#page from next button
    items = get_page(page)#attribute page get start and end of the given books
    if not items:#check if items is empty
        await callback.answer("🚫 Bu oxirgi sahifa", show_alert=True)#if not exist , it show wrong
        return

    text = "\n".join([f"{i+1}. {item}" for i, item in enumerate(items)])#formating string to good view
    markup = search_title(book_id, count=page)#back page number next cancel send
    markup2 = select_buttons(book_id, page)#button from 1 to need number
    #cobine two buttons
    full_markup = InlineKeyboardMarkup(
        inline_keyboard=markup2.inline_keyboard + markup.inline_keyboard
    )

    await callback.message.edit_text(text, reply_markup=full_markup)#transform old message to new
    await callback.answer()#I dont undestand

@search_router.callback_query(F.data.startswith("back_"))
async def back_page(callback: types.CallbackQuery):
    _, book_id, page = callback.data.split("_")
    page = int(page)
    if page < 1:
        await callback.answer("🚫 Bu birinchi sahifa", show_alert=True)
        return

    items = get_page(page)
    text = "\n".join([f"{i+1}. {item}" for i, item in enumerate(items)])

    markup = search_title(book_id, count=page)
    markup2 = select_buttons(book_id, page)

    full_markup = InlineKeyboardMarkup(
        inline_keyboard=markup2.inline_keyboard + markup.inline_keyboard
    )

    await callback.message.edit_text(text, reply_markup=full_markup)
    await callback.answer()

# @search_router.callback_query(F.data.startwith("select_"))
# async def send_books(call:CallbackQuery):
#     book_id = call.data
