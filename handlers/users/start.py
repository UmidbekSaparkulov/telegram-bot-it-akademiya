import logging
from aiogram.types import ReplyKeyboardRemove
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.til_keyboard import menutil
from loader import dp

@dp.message_handler(CommandStart())
async def botstart(message: types.Message):
    # logging.info(message)
    # logging.info(f"{message.from_user.username=}")
    # logging.info(f"{message.from_user.full_name=}")
    # users = {message.from_user.id:message.from_user.username}
    await message.answer(f"Assalomu alleykum hurmatli foydalanuvchi🧑‍🎓👨🏻‍🎓\n\n (Здравствуйте Уважаемый пользователь) <b>{message.from_user.username}👨🏻‍💻</b>! \n\n\n tilni tanlang/выберите язык (uz/rus) ", reply_markup=menutil)
    

    