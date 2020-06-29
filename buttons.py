from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


button_plus = KeyboardButton('1️⃣')

markup = ReplyKeyboardMarkup().row(button_plus)
