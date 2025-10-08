from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def search_title(book_id):
    count=1
    search_by_title = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text='◀️ Back',callback_data=f"back_{book_id}_{count}"), InlineKeyboardButton(text=f"{count}",callback_data=f"number"),InlineKeyboardButton(text="Next ▶️",callback_data=f"next__{book_id}_{count}")],

            [InlineKeyboardButton(text="Cancel ❌",callback_data="cancel"),InlineKeyboardButton(text="Send 🚀",callback_data=f"send_{book_id}")]
        ]
    )
    return search_by_title