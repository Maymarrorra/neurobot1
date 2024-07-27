from aiogram import types

button1 = types.KeyboardButton(text="/start")
button2 = types.KeyboardButton(text="/stop")
button3 = types.KeyboardButton(text="Marco")
button4 = types.KeyboardButton(text="Polo")
button5 = types.KeyboardButton(text="Show the fox")
botton6 = types.KeyboardButton(text="/prof")

keyboard1 = [
    [button1, button2, button3],
    [button4, button5, botton6],
]

kb1 = types.ReplyKeyboardMarkup(keyboard = keyboard1, resize_keyboard=True)