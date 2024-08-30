from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
ru_menucategory = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🏫 Трамплин Ит академия ", callback_data='ru_o_markaz'),
            InlineKeyboardButton(text="💻 Курси", callback_data='ru_cours')
        ],
        [
            InlineKeyboardButton(text="👨🏼‍💼 Известные люди в программировании ", callback_data='ru_hodimlar'),
            InlineKeyboardButton(text="💼 Вакансии", callback_data='ru_vakansiya')
        ],
        [
            InlineKeyboardButton(text="☎️ Контактный номер телефона",url='https://t.me/tramplin_uz')
        ]
    ]
)
ru_courses_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text=" Бэкэнд курс ", callback_data='ru_back_c'),
            InlineKeyboardButton(text=" Курс по фронтенду", callback_data='ru_fcours'),
        ],
        [
            InlineKeyboardButton(text=" Курс мобильной графики", callback_data='ru_mgcours'),
            InlineKeyboardButton(text=" Курс кибербезопасности", callback_data='ru_cybcours')
        ],
        [
            InlineKeyboardButton(text="⤴️ Назад", callback_data='ru_ortga')
        ]
    ]
)

ru_informatsiya = InlineKeyboardMarkup(
    inline_keyboard = [
        [
            InlineKeyboardButton(text="⤴️ Назад", callback_data='ru_ortga')
        ]
    ]
)
#  Cours uchun tugmalar
ru_backend_course = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="⤴️ Назад", callback_data='cru_ortga')]])
ru_frontend_course = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="⤴️ Назад", callback_data='cru_ortga')]])
ru_Kiberxavfsizlik_course = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="⤴️ Назад", callback_data='cru_ortga')]])
ru_mobilagrafik_course = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="⤴️ Назад", callback_data='cru_ortga')]])


ru_hodimlar_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Сундар Пичаи', callback_data='ru_google_direktori'),
            InlineKeyboardButton(text="Павел Валерьевич Дуров", callback_data='ru_telegram_asoschisi'),
        ],
        [
            InlineKeyboardButton(text="Аркадий Юрьевич Волож", callback_data='ru_yandeks_asoschisi'),
            InlineKeyboardButton(text="Джеффри Престон Йоргенсен", callback_data='ru_amazon_asoschisi'),
        ],
        [
            InlineKeyboardButton(text="⤴️ Назад", callback_data='ru_ortga')
        ]
    ]
)

ru_murojaat_uchunKeyboard = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='⤴️ Назад', callback_data='ru_ortga')]])
ru_hodim_ortga_tugma = InlineKeyboardMarkup(inline_keyboard=[[
            InlineKeyboardButton(text="⤴️ Назад", callback_data='rug_ortga')
        ]])