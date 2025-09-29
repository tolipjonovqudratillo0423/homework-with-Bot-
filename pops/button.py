from aiogram.types import ReplyKeyboardMarkup, KeyboardButton   

register_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Register")]
    ],
    resize_keyboard=True
)

share_phone_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Share phone number", request_contact=True)]
    ],
    resize_keyboard=True, 
    one_time_keyboard=True
)

location_share_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Share location", request_location=True)]
    ],
    resize_keyboard=True, 
    one_time_keyboard=True
)


