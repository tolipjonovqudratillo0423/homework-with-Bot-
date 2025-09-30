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

