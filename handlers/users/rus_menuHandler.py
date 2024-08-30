import logging

from aiogram.types import Message, CallbackQuery
from loader import dp
from keyboards.inline.rus_menu import ru_hodimlar_keyboard, ru_hodim_ortga_tugma
from keyboards.inline.rus_menu import ru_menucategory, ru_courses_menu, ru_backend_course, ru_informatsiya, ru_frontend_course, ru_mobilagrafik_course, ru_Kiberxavfsizlik_course
from keyboards.default.til_keyboard import menutil
from aiogram.types import InputFile
from aiogram.types import ReplyKeyboardRemove

@dp.message_handler(text_contains="Руссиа")
async def menu_select(message: Message):
    # ReplyKeyboardRemove bilan klaviaturani o'chirish
    await message.answer("🇷🇺 язык выбран",reply_markup=ReplyKeyboardRemove())
    
    photo_url = InputFile(path_or_bytesio="handlers/Photos_oquvmarkaz/tramplin_photomarkaz.png")
    habar = "<b>Учебный сентр на информатсия </b>\n\n"
    habar += "В Трамплин IT Academy вы можете изучать программирование у профессионалов.\n"
    habar += "В ходе курса вы сможете пройти качественное обучение у высококвалифицированных программистов по специальной методике и создать собственное портфолио на основе более чем 50 проектов, используя полученные знания."
    await message.delete()
    await message.answer_photo(photo=photo_url, caption=habar, reply_markup=ru_menucategory)
    
@dp.callback_query_handler(text="ru_cours")
async def select_courses(call: CallbackQuery):
    photo_url1 = InputFile(path_or_bytesio="handlers/zamonaviy_kasblar/zamonaviykasblar.jpg")
    msg="Выбери одну из современных профессий"
    await call.message.answer_photo(photo=photo_url1, caption=msg, reply_markup=ru_courses_menu)
    await call.message.delete()

@dp.callback_query_handler(text="ru_ortga")
async def cancel_buying(call: CallbackQuery):
    photo_url = InputFile(path_or_bytesio="handlers/Photos_oquvmarkaz/tramplin_photomarkaz.png")
    habar = "<b>Учебный сентр на информатсия </b>\n\n"
    habar += "В Трамплин IT Academy вы можете изучать программирование у профессионалов.\n"
    habar += "В ходе курса вы сможете пройти качественное обучение у высококвалифицированных программистов по специальной методике и создать собственное портфолио на основе более чем 50 проектов, используя полученные знания."
    
    
    await call.message.answer_photo(photo=photo_url, caption=habar, reply_markup=ru_menucategory)
    await call.message.delete()

    


@dp.callback_query_handler(text="ru_back_c")
async def courses(call:CallbackQuery):
    
    video_url = InputFile(path_or_bytesio="handlers/videobackend/.backendkurs.mp4")
    await call.message.answer_video(video=video_url, caption="Курс «Бэкэнд-разработка на Питон» состоит из нескольких модулей, охватывающих различные аспекты разработки веб-приложений и ботов Telegram.", reply_markup=ru_backend_course)
    await call.message.delete()
@dp.callback_query_handler(text="ru_fcours")
async def courses(call:CallbackQuery):

    video_url = InputFile(path_or_bytesio="handlers\Frontendkursi\FrontendCoursi.mp4")
    await call.message.answer_video(video=video_url, caption="<b>Фронтенду</b> bu Это одна из областей веб-программирования, то есть с помощью <b>Frontend</b> вы создаете ту часть веб-сайта, которая видна пользователям.", reply_markup=ru_frontend_course)
    await call.message.delete()

@dp.callback_query_handler(text="ru_mgcours")
async def courses(call:CallbackQuery):

    video_url = InputFile(path_or_bytesio="handlers\Mobilografiyakursi\mobilografiyakursi'.mp4")
    await call.message.answer_video(video=video_url, caption="<b>графический дизайн</b> — одно из направлений сферы дизайна, которое служит для создания, сортировки и оформления визуального контента для донесения определенной информации до социальных групп. ", reply_markup=ru_mobilagrafik_course)
    await call.message.delete()

@dp.callback_query_handler(text="ru_cybcours")
async def courses(call:CallbackQuery):

    video_url = InputFile(path_or_bytesio="handlers/Kiberxafsizlikcoursi/Ciberafsizlikcoursi.mp4")
    await call.message.answer_video(video=video_url, caption="...сетевая безопасность связана с поддержанием мира в крепостных стенах и защитой суверенитета организации от сетевых угроз.", reply_markup=ru_Kiberxavfsizlik_course)
    await call.message.delete()



@dp.callback_query_handler(text="cru_ortga")
async def cancel_courses(call:CallbackQuery):
    photo_urlortga = InputFile(path_or_bytesio="handlers/zamonaviy_kasblar/zamonaviykasblar.jpg")
    await call.message.answer_photo(photo=photo_urlortga, reply_markup=ru_courses_menu) 
    await call.message.delete()


@dp.callback_query_handler(text="ru_o_markaz")
async def markaz_informatsion(call:CallbackQuery):
    photo_url = InputFile(path_or_bytesio="handlers/Photos_oquvmarkaz/tramplin_photomarkaz.png")

    msg = "<b>Информация об образовательном центре</b>\nВ Трамплин ИТ Academy вы можете учиться у профессионалов.\n\n\n"
    msg += "Курс качественный, основанный на специальной методике от высококвалифицированных программистов.\n<b>50</b> в обучении и совершенствовании своих знаний\n"
    msg += "Вы можете создать свое собственное портфолио.\n\n\n"
    msg += "Мы обеспечиваем трудоустройство, если:\n\n\n"
    msg += "<b> -Интервью</b>\n"
    msg += "<b> -Обязанности</b>\n"
    msg += "<b> - Экзамен</b>\n"
    msg += "<b> - Презентация книги.</b>\n"
    msg += "<b> -Мини.</b>\n\n\n"
    msg += "если вы получите <b>90/100</b> из вышеперечисленного\n\n\n"
    msg += "📞 Связаться с нами: <b>+9989 (90) 805-51-95</b>\n\n"
    msg += "📍<b> г.Ташкент, улица Амира Темура, 47, возле метро Ташкентское</b>\n\n"
    msg += "🌐 телеграмм канал: <b> hhtps://t.me/tramplin_uz</b>"


    await call.message.delete()
    await call.message.answer_photo(photo=photo_url, caption=msg, reply_markup=ru_informatsiya)



# Xodimlar uchun handler 

@dp.callback_query_handler(text="ru_hodimlar")
async def hodimlar_information(call: CallbackQuery):
    file_rasm = InputFile(path_or_bytesio="handlers/ijtimoiy_tarmoq/rasmlar.png")
    await call.message.answer_photo(photo=file_rasm, reply_markup=ru_hodimlar_keyboard)
    await call.message.delete()

# google uchun

@dp.callback_query_handler(text="ru_google_direktori")
async def google_inouz(call:CallbackQuery):
    ru_googleAs = InputFile(path_or_bytesio="handlers/googleAsoschisi/google_asoschisi.jpg")

    msg = "Красивая жизнь не приходит сама собой. Это результат учебы, постоянного стремления и упорного труда.\nЭто наиболее подходящее определение счастливой жизни. Иначе, в отдаленном южноиндийском городе Мадурай,\n"
    msg += "ребенок, родившийся в обычной семье, не стал бы одним из самых высокооплачиваемых руководителей за океаном в 2016 году.\n"
    msg += "В 2015 году Alphabet Inc., владеющая Google. После создания холдинга главой Google будет назначен индийский уроженец <b>Сундар Пичаи</b>.\n"
    msg += "<b>Сундар Пичаи</b> родился в 1972 году в штате Тамил Наду, Индия, в семье инженера-электрика.\n"
    msg += "Будущего главу Google отличала от сверстников тяга к знаниям с юных лет.\n В школе он был застенчивым учеником, мало говорил, но его слова были полны смысла. Электроника\nшпионаж был его любимым занятием. Его называют гением компании, приносящей облегчение в жизнь человека."
    await call.message.delete()
    await call.message.answer_photo(photo=ru_googleAs, caption=msg, reply_markup=ru_hodim_ortga_tugma)

@dp.callback_query_handler(text="ru_telegram_asoschisi")
async def telegram_inouz(call:CallbackQuery):
    ru_telegramAs = InputFile(path_or_bytesio="handlers/telagram_Asoschisi/tg_asoschisi.jpg")
    msg2 = "<b>Павел Валерьевич Дуров</b>\n Русский: Павел Валерьевич Дуров; Родился 10 октября 1984 года.\n Родился в России, бизнес-менеджер Telegram Messenger Inc.\n соучредитель, генеральный директор и соучредитель.\n"
    msg2 += "аббревиатура оригинального названия сайта социальной сети ВК ВКонтакте; Русский: ВКонтакте означает InContact.\n По состоянию на 2021 год он имеет гражданство четырех стран и Европейского Союза.\n"
    await call.message.delete()
    await call.message.answer_photo(photo=ru_telegramAs, caption=msg2, reply_markup=ru_hodim_ortga_tugma)
                                    

@dp.callback_query_handler(text="ru_yandeks_asoschisi")
async def yandexs_inouz(call:CallbackQuery):
    ru_yandeksAs = InputFile(path_or_bytesio="handlers/Yandeks_asoschisir/yandeks_asoschisi.webp")
    msg3 = "<b>Павел Валерьевич Дуров</b>\n Русский: Павел Валерьевич Дуров; Родился 10 октября 1984 года. \nРодился в России, бизнес-менеджер Telegram Messenger Inc.\n соучредитель, генеральный директор и соучредитель.\n"
    msg3 += "аббревиатура оригинального названия сайта социальной сети ВК ВКонтакте; Русский: ВКонтакте означает InContact.\n По состоянию на 2021 год он имеет гражданство четырех стран и Европейского Союза.\n"
    await call.message.delete()
    await call.message.answer_photo(photo=ru_yandeksAs, caption=msg3, reply_markup=ru_hodim_ortga_tugma)

@dp.callback_query_handler(text="ru_amazon_asoschisi")
async def amazon_inouz(call:CallbackQuery):
    ru_amazonAs = InputFile(path_or_bytesio="handlers/amazon_asoschisid/amazon_asoschisi.jpg")
    msg4 = "<b>Павел Валерьевич Дуров</b>\n Русский: Павел Валерьевич Дуров; Родился 10 октября 1984 года. Родился в России, бизнес-менеджер Telegram Messenger Inc.\n соучредитель, генеральный директор и соучредитель.\n"
    msg4 += "аббревиатура оригинального названия сайта социальной сети ВК ВКонтакте; Русский: ВКонтакте означает InContact.\n По состоянию на 2021 год он имеет гражданство четырех стран и Европейского Союза.\n"
    msg4 += "24 августа 2024 года Дуров был арестован во Франции по обвинению в отсутствии модерации контента в Telegram и отказе сотрудничать с полицией, что способствовало распространению преступной деятельности."

    await call.message.delete()
    await call.message.answer_photo(photo=ru_amazonAs, caption=msg4, reply_markup=ru_hodim_ortga_tugma)

@dp.callback_query_handler(text="rug_ortga")
async def cancel_buying(call: CallbackQuery):
    file_rasm = InputFile(path_or_bytesio="handlers/ijtimoiy_tarmoq/rasmlar.png")
    await call.message.answer_photo(photo=file_rasm, reply_markup=ru_hodimlar_keyboard)
    await call.message.delete()
