from aiogram import Router, types, F
from aiogram.filters.command import Command
from less3.keyboards.keyboards import kb1
from less3.utils.randomfox import fox
from random import randint

router = Router()


@router.message(Command("start"))
async def command_start(message: types.Message):
    name = message.chat.first_name
    await message.answer(f'Привет, {name}', reply_markup=kb1)


@router.message(Command("stop"))
async def command_stop(message: types.Message):
    name = message.chat.first_name
    await message.answer(f'Пока, {name}')


@router.message(Command("fox"))
@router.message(F.text.lower() == 'show the fox')
@router.message(F.text.lower() == 'fox')
async def command_fox(message: types.Message):
    name = message.chat.first_name
    img_fox = fox()
    await message.answer(f'Here is your fox, {name}')
    await message.answer_photo(photo=img_fox)
    #await bot.send_photo(message.from_user.id, photo=img_fox)


@router.message(F.text.lower() == 'num')
async def send_random(message: types.Message):
    number = randint(a=1, b=10)
    await message.answer(f'{number}')


@router.message(F.text)
async def msg_echo(message: types.Message):
    msg_user = message.text
    if "Marco" in msg_user:
        await message.answer('Polo')
    elif "Polo" in msg_user:
        await message.answer('Marco')
    elif "Info" in msg_user:
        await message.answer("Hey! Let's play Marco Polo. You say Marco - I say Polo")
    else:
        await message.answer(f'Simon says {msg_user}')


