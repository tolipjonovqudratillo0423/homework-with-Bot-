from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup


# BU REGISTATSIYA UCHUN REPLY BUTTON !!!!! BOSHIDA CHIQADI
register_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="📝 Register")]
            ],
            resize_keyboard=True,
            one_time_keyboard=True
    
)
#TELEFON ULASHISH
share_phone_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="📞 Provide phone number", request_contact=True)]
    ],
    resize_keyboard=True, 
    one_time_keyboard=True
)
#LOCATION ULASHISH
location_share_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text=" 📍 Share my location", request_location=True)]
    ],
    resize_keyboard=True, 
    one_time_keyboard=True
)
#KEYINGI
continue_button = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="➡️ Continue")]
    ],
    resize_keyboard=True, 
    one_time_keyboard=True
)
#BU MENU BUTTON REPLY: BOOK ORDER PROFIL CONTACT BUTTON BOR
menu_kb= ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="📚 Books"),KeyboardButton(text="👤 Profile")],
        [KeyboardButton(text="📝 Order"),KeyboardButton(text="📞 Contact")]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)
#BACK
back_kb= ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="↩️ Back")]

    ],
    resize_keyboard=True,
    one_time_keyboard=True
)
#MENU DAGI BOOK BUTTONGA BOSILGANDA CHIQADIGAN BUTTON 
books_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🔎 Search"), KeyboardButton(text="📚 All")],
        [KeyboardButton(text="✨ New"), KeyboardButton(text="💸 Discounted books")],
        [KeyboardButton(text="↩️ Back")]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)
#MENU PROFIL BUTTON
profile_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="✏️ Change username"), KeyboardButton(text="📍 Change location")],
        [KeyboardButton(text="📞 Change phone number"),KeyboardButton(text="👤 About Me")],
        [KeyboardButton(text="↩️ Back")]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)
#MENU ORDER BUTTON 
order_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🛒 Ordered Books")],
        [KeyboardButton(text="↩️ Back")]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)
#BU BOOK BUTTONIDAGI SEARCH BUTTON BOSILSA CHIQADIGAN BUTTON 
search_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🔎 Search by Title"), KeyboardButton(text="🔎 Search by Author")],
        [KeyboardButton(text="🔎 Search by Genre")],
        [KeyboardButton(text="↩️ Back")]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)
#BU BUTTON SEARCH JARAYONI TUGAGANDAN KEYIN CHIQADIGA INLINE BUTTON 
search_plus_minus_inb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="➖",callback_data="decreacse"),InlineKeyboardButton(text="❌",callback_data="cancel"),InlineKeyboardButton(text="➕",callback_data="add")],
        [InlineKeyboardButton(text="❌",callback_data="broke"),InlineKeyboardButton(text="✅",callback_data="confirm")]
    ],
    
)

