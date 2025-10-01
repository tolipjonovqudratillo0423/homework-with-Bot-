from aiogram.types import ReplyKeyboardMarkup, KeyboardButton   

register_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="📝 Register")]
            ],
            resize_keyboard=True,
            one_time_keyboard=True
    
)

share_phone_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="📞 Provide phone number", request_contact=True)]
    ],
    resize_keyboard=True, 
    one_time_keyboard=True
)

location_share_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text=" 📍 Share my location", request_location=True)]
    ],
    resize_keyboard=True, 
    one_time_keyboard=True
)

continue_button = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="➡️ Continue")]
    ],
    resize_keyboard=True, 
    one_time_keyboard=True
)
menu_kb= ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="📚 Books"),KeyboardButton(text="👤 Profile")],
        [KeyboardButton(text="📝 Order"),KeyboardButton(text="📞 Contact")]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)
back_kb= ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="↩️ Back")]

    ],
    resize_keyboard=True,
    one_time_keyboard=True
)
books_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🔎 Search"), KeyboardButton(text="📚 All")],
        [KeyboardButton(text="✨ New"), KeyboardButton(text="💸 Discounted books")],
        [KeyboardButton(text="↩️ Back")]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)

profile_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="✏️ Change username"), KeyboardButton(text="📍 Change location")],
        [KeyboardButton(text="📞 Change phone number"),KeyboardButton(text="👤 About Me")],
        [KeyboardButton(text="↩️ Back")]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)

order_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🛒 Ordered Books")],
        [KeyboardButton(text="↩️ Back")]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)
search_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🔎 Search by Titlte"), KeyboardButton(text="🔎 Search by Author")],
        [KeyboardButton(text="🔎 Search by Genre")],
        [KeyboardButton(text="↩️ Back")]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)

