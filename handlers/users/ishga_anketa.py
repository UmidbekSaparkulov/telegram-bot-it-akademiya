import logging

from aiogram import types
from aiogram.types import Message, CallbackQuery, InputFile
from aiogram.dispatcher import FSMContext

from loader import dp
from states.personalData import PersonalData
from keyboards.inline.uzb_menu import informatsiya, menucategory

@dp.callback_query_handler(text="vakansiya")
async def enter_text(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("Qaysi yo'nalish bo'yicha ishlamoqchisiz:")
    await PersonalData.qaysi_sohaga.set()

@dp.message_handler(state=PersonalData.qaysi_sohaga)
async def answer_soha(message: Message, state: FSMContext):
    soha = message.text

    await state.update_data(
        {
            'soha tanlandi': soha
        }
    )
    await message.answer("To'liq ism sharifingizni kiriting:")
    await PersonalData.fullname.set()

@dp.message_handler(state=PersonalData.fullname)
async def answer_fullname(message: Message, state: FSMContext):
    fullname = message.text

    await state.update_data(
        {
            'F.I.O': fullname
        }
    )
    await message.answer("Rezyumeni yuboring:")
    await PersonalData.next()

@dp.message_handler(content_types=types.ContentType.DOCUMENT, state=PersonalData.resume)
async def answer_resume(message: Message, state: FSMContext):
    resume = message.document

    await state.update_data(
        {
            'resume': resume.file_name
        }
    )
    await message.answer("Telefon raqamingizni yuboring:")
    await PersonalData.next()

@dp.message_handler(state=PersonalData.phoneNumber)
async def answer_phone(message: Message, state: FSMContext):
    phone = message.text

    await state.update_data(
        {
            'telefon nomer': phone
        }
    )
    
    data = await state.get_data()
    soha = data.get('soha tanlandi')
    fullname = data.get('F.I.O')
    resume = data.get('resume')
    phone = data.get('telefon nomer')

    msg = (
        "Quyidagi ma'lumotlar qabul qilindi.\n"
        "Tez orada operatorlarimiz bog'lanadi.\n\n\n"
        f"<b>Topshirgan yo'nalshingiz</b>: {soha}\n"
        f"<b>ism familiya sharifi</b>: {fullname}\n"
        f"<b>Rezyumengiz</b>: {resume}\n"
        f"<b>Telefon raqamingiz</b>: {phone}"
    )

    
    await state.finish()
    await state.reset_state(with_data=False)
    await message.answer(msg, reply_markup=informatsiya)

@dp.callback_query_handler(text="1ortga")
async def cancel_buying(call: CallbackQuery):
    photo_url = InputFile(path_or_bytesio="handlers/Photos_oquvmarkaz/tramplin_photomarkaz.png")
    habar = "<b>Tramplin IT Akademiyasi haqida qisqacha ma'lumot</b>\n\n"
    habar += "Tramplin IT Akademiyasida siz Dasturlashni professionallardan o'rganishingiz mumkin.\n"
    habar += "Kurs davomida yuqori malakali dasturchilardan maxsus metodika asosida sifatli ta’lim olishingiz va o'zlashtirgan bilimlaringizni amaliyotda 50 dan ortiq loyiha asosida o'z portfolioingizni yaratishingiz mumkin."
    await call.message.answer_photo(photo = photo_url, caption=habar, reply_markup=menucategory)
    
